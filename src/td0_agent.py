
import numpy as np
import time
from typing import List, Tuple, Optional

from game2048 import (
    new_board, add_random_tile, apply_move, is_terminal,
    get_valid_moves, spawn_probability, max_tile, left,up,right,down
)
from ntuple_network import NTupleNetwork

"""
The game runs past 2048 — no win condition — to match the paper's setup
and measure how high the agent can actually go.
"""


def select_move(board: np.ndarray, net: NTupleNetwork) -> Tuple[int, np.ndarray, int]:
    """
    Choose the move that maximises immediate reward plus expected future value. THIS IS ONE-PLY
    Returns (direction, afterstate, score).
    """
    best_q = -np.inf
    best_dir= -1
    best_afterstate = None
    best_score = 0
    #Expectimax Implentation
    for direction in get_valid_moves(board):
        afterstate, score, _ = apply_move(board, direction)
        spawns = spawn_probability(afterstate)
        expected_v = sum(p * net.evaluate(b) for b, p in spawns) if spawns else 0.0
        q= score + expected_v
        if q > best_q:
            best_q = q
            best_dir= direction
            best_afterstate = afterstate
            best_score = score

    return best_dir, best_afterstate, best_score




def td_update(net:NTupleNetwork, afterstate: np.ndarray, reward:int,next_afterstate: Optional[np.ndarray],alpha:float,
    terminal:bool,) -> None:
    """
    TD(0) update 
    """
    v_current = net.evaluate(afterstate)
    v_next= 0.0 if terminal else net.evaluate(next_afterstate)
    delta = reward + v_next - v_current
    net.update(afterstate, delta, alpha)




def run_episode(net: NTupleNetwork, alpha: float, rng: np.random.Generator) -> Tuple[int, int]:
    """
   Play a game for s&gs
    """
    board = add_random_tile(add_random_tile(new_board(), rng), rng)
    total_score = 0

    while not is_terminal(board):
        direction, afterstate, score = select_move(board, net)
        next_board = add_random_tile(afterstate, rng)
        total_score += score

        if is_terminal(next_board):
            td_update(net, afterstate, score, None, alpha, terminal=True)
        else:
            next_dir, next_afterstate, _ = select_move(next_board, net)
            td_update(net, afterstate, score, next_afterstate, alpha, terminal=False)

        board = next_board

    return total_score, max_tile(board)



def train(episodes: int= 50_000, alpha:float = 0.1, eval_every:int = 1_000, eval_games:int = 200,
    checkpoint_every: int= 10_000, checkpoint_path:str= "td0_checkpoint",seed:int   = 42,) -> Tuple[NTupleNetwork, dict]:
    """
    Train the TD(0) baseline agent.

    """
    rng = np.random.default_rng(seed)
    net = NTupleNetwork()
    print(f"TD(0) baseline | {net}")
    print(f"Training {episodes:,} episodes, alpha={alpha}\n")

    history = {
        "scores":[],  # per-episode training score
        "tiles":[],   # per-episode max tile
        "eval_scores": [],   # mean score at each eval point
        "eval_tiles":  [],   # mean max tile at each eval point
        "eval_at":     [],   # episode numbers of eval points
    }

    t0 = time.time() #see how long this takes 

    for ep in range(1, episodes + 1):
        score, tile = run_episode(net, alpha, rng)
        history["scores"].append(score)
        history["tiles"].append(tile)

        if ep % eval_every == 0:
            e_scores, e_tiles = evaluate(net, eval_games, rng=rng)
            history["eval_scores"].append(float(np.mean(e_scores)))
            history["eval_tiles"].append(float(np.mean(e_tiles)))
            history["eval_at"].append(ep)

            elapsed= time.time() - t0
            speed= ep / elapsed
            win_pct= 100 * np.mean([t >= 2048 for t in e_tiles])
            roll_avg = np.mean(history["scores"][-eval_every:])
            best= max(history["tiles"][-eval_every:])

            print(
                f"ep {ep:>7,} | "
                f"train {roll_avg:>8,.0f} | "
                f"eval {np.mean(e_scores):>8,.0f} | "
                f">=2048: {win_pct:4.1f}% | "
                f"best: {best:>5} | "
                f"{speed:>5.0f} ep/s")

        if checkpoint_every > 0 and ep % checkpoint_every == 0:
            net.save(f"{checkpoint_path}_ep{ep}")
    elapsed = time.time() - t0
    print(f"\nDone: {episodes:,} episodes in {elapsed/60:.1f} min "
          f"({episodes/elapsed:.0f} ep/s)")
    print(f"Table coverage: {net.nonzero_ratio():.1%} of entries trained")
    return net, history

def evaluate(net:NTupleNetwork,episodes: int = 1_000, rng:Optional[np.random.Generator] = None,
    seed: int = 0,) -> Tuple[List[int], List[int]]:
    """
    Play episodes games(expectimax
    Returns (scores, max_tiles).
    """
    if rng is None:
        rng = np.random.default_rng(seed)
    scores, tiles = [], []
    for ep in range(episodes):
        board = add_random_tile(add_random_tile(new_board(), rng), rng)
        total_score = 0

        while not is_terminal(board):
            direction, afterstate, score = select_move(board, net)
            total_score += score
            board= add_random_tile(afterstate, rng)

        scores.append(total_score)
        tiles.append(max_tile(board))

    return scores, tiles


def report(scores: List[int], tiles: List[int], label: str = "Agent") -> str:
    s = np.array(scores)
    t = np.array(tiles)
    lines = [
        f"── {label} ── ({len(scores)} games)",
        f"  Score mean={s.mean():>10,.0f}  std={s.std():>9,.0f}  max={s.max():>10,}",
        f"  Tile mean={t.mean():>10,.0f}  max={int(t.max()):>6,}",
        "  Reach" + "  ".join(
            f">={v}: {100*np.mean(t>=v):4.1f}%"
            for v in [256, 512, 1024, 2048, 4096]
        ),
        "  Distribution:",
    ]
    vals, counts = np.unique(t, return_counts=True)
    for v, c in zip(vals, counts):
        bar = "█" * int(40 * c / len(scores))
        lines.append(f"{int(v):>6}: {int(c):>4}  {bar}")
    return "\n".join(lines)


if __name__ == "__main__":
    net, history = train(episodes= 50_000,
        alpha= 0.1,
        eval_every= 2_000,
        eval_games = 200,
        checkpoint_every= 10_000,
        checkpoint_path = "td0",
        seed= 811,
    )

    net.save(f"td0_final_512")

    print("\nFinal evaluation (1,000 games):")
    scores, tiles = evaluate(net, 1_000)
    print(report(scores, tiles, "TD(0) baseline"))
