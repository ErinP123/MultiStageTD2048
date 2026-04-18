
import numpy as np
import time
from typing import List, Tuple, Optional

from game2048 import (
    new_board, add_random_tile, apply_move, is_terminal,
    get_valid_moves, spawn_probability, max_tile, max_tile_exp,
)
from ntuple_network import NTupleNetwork
from td0_agent import select_move, evaluate, report



#This is the halfway point so chose this to go from stage 1 to stage 2
boundary = 1024   



def make_stage2_board(rng: np.random.Generator) -> np.ndarray:
    """
   Need to make a board for game to pick up from (it wont be a null board)
    """
    from game2048 import new_board
    board = new_board()
    # set up configuration to learn off of
    config = [
        (0, 10), (1, 9), (2, 8), (3, 7),
        (4, 6),  (5, 5), (6, 4), (7, 3),
        (8, 2),  (9, 2), (10, 1), (11, 1),
        (12, 1), (13, 1),
    ]
    for idx, exp in config:
        board[idx] = exp
    # Add 1-2 random small tiles in empty spots
    empty = np.where(board == 0)[0]
    if len(empty) > 0:
        chosen = rng.choice(empty, size=min(2, len(empty)), replace=False)
        for c in chosen:
            board[c] = rng.choice([1, 2])
    return board


def get_stage(board: np.ndarray) -> int:
    """
    Return 1 or 2 based on the highest tile currently on the board.
    Stage 1: max tile <  boundary  (Early game)
    Stage 2: max tile >= boundary  (Later)
    """
    return 1 if max_tile(board) < boundary else 2


'''I set this up like the pacman projects '''

class MultiStageAgent:
    """
    Holds both stage networks and routes evaluations to the right one.
    Both networks are NTupleNetwork instances with the same architecture.
    """

    def __init__(self):
        self.nets = {
            1: NTupleNetwork(),
            2: NTupleNetwork(),
        }

    def evaluate(self, board: np.ndarray) -> float:
        """Evaluate using the network for the current stage."""
        return self.nets[get_stage(board)].evaluate(board)

    def active_net(self, board: np.ndarray) -> NTupleNetwork:
        return self.nets[get_stage(board)]

    def save(self, prefix: str) -> None:
        self.nets[1].save(f"{prefix}_stage1")
        self.nets[2].save(f"{prefix}_stage2")

    @classmethod
    def load(cls, prefix: str) -> "MultiStageAgent":
        agent = cls()
        agent.nets[1] = NTupleNetwork.load(f"{prefix}_stage1")
        agent.nets[2] = NTupleNetwork.load(f"{prefix}_stage2")
        return agent




def select_move_ms(board: np.ndarray, agent: MultiStageAgent) -> Tuple[int, np.ndarray, int]:
    """
    One-ply expectiminimax using the stage-appropriate network.

    For each legal move:
        Q = score + E_tile[ V_stage(board_after_spawn) ]

    The stage is determined by the CURRENT board (before the move).
    After a tile spawn, if the spawn>max(512, 1028), swap to Stage2
    """
    #Start reallllly low
    best_q          = -np.inf
    best_dir        = -1
    best_afterstate = None
    best_score      = 0

    for direction in get_valid_moves(board):
        afterstate, score, _ = apply_move(board, direction)

        spawns = spawn_probability(afterstate)
        expected_v = sum(p * agent.evaluate(b) for b, p in spawns) if spawns else 0.0
        q = score + expected_v

        if q > best_q:
            best_q          = q
            best_dir        = direction
            best_afterstate = afterstate
            best_score      = score
    ##Get move with. the best possibly outcome 
    return best_dir, best_afterstate, best_score


def td_update_ms(agent: MultiStageAgent, afterstate: np.ndarray,reward: int,
    next_afterstate: Optional[np.ndarray],alpha:float,terminal:bool,current_stage:int,) -> None:

    net = agent.nets[current_stage]
    v_current = net.evaluate(afterstate)

    if terminal or next_afterstate is None:
        v_next = 0.0
    else:
        # Route bootstrap to whichever network owns the next afterstate
        v_next = agent.evaluate(next_afterstate)
    #if we're toooooo low make it higher and if we're tooo high make it lower
    delta = reward + v_next - v_current
    net.update(afterstate, delta, alpha)


#Trains Specific Stage 

def run_episode_stage(agent:MultiStageAgent,target_stage:int, alpha:float,rng:np.random.Generator,
) -> Tuple[int, int, bool]:
    """
    Update Target
    For stage 2 training: updates happen on every move where the board
        is already in Stage 2.
    For stage 1 training: updates happen on Stage 1 moves. 

    Returns (total_score, max_tile, crossed_boundary).
    crossed_boundary = True if the game ever reached Stage 2.
    """
    # Stage 1 starts from a fresh board as normal.
    if target_stage == 2:
        board = make_stage2_board(rng)
    else:
        board = add_random_tile(add_random_tile(new_board(), rng), rng)

    total_score = 0
    crossed_boundary  = False

    while not is_terminal(board):
        current_stage  = get_stage(board)
        direction, afterstate, score = select_move_ms(board, agent)
        next_board= add_random_tile(afterstate, rng)
        total_score+= score

        if max_tile(afterstate) >= boundary:
            crossed_boundary = True

        # Only update the network we are currently training
        if current_stage == target_stage:
            if is_terminal(next_board):
                td_update_ms(agent, afterstate, score, None,
                             alpha, terminal=True, current_stage=current_stage)
            else:
                next_dir, next_afterstate, _ = select_move_ms(next_board, agent)
                td_update_ms(agent, afterstate, score, next_afterstate,
                             alpha, terminal=False, current_stage=current_stage)

        board = next_board

    return total_score, max_tile(board), crossed_boundary




def train_multistage(stage2_episodes:int= 30_000, stage1_episodes:int = 30_000,alpha:            float = 0.1,
    eval_every:int= 1_000, eval_games:int= 200, checkpoint_every: int= 10_000,
    checkpoint_prefix: str = "ms",seed:int= 811,
) -> Tuple[MultiStageAgent, dict]:
    """
    Train the multi-stage agent in reverse order:
        1. Train Stage 2 (Board>1024) — no cross-stage bootstrap
        2. Train Stage 1 (board<1024) — uses  Stage 2 

    Returns (agent, history).
    """
    rng   = np.random.default_rng(seed)
    agent = MultiStageAgent()

    history = {
        "s2_scores": [], "s2_tiles": [],
        "s1_scores": [], "s1_tiles": [],
        "eval_scores": [], "eval_tiles": [], "eval_at": [],
    }

    print("*-" * 60)
    print(f"Phase 1: Training Stage 2 (max tile >= {boundary})")
    print(f"{stage2_episodes:,} episodes, alpha={alpha}")
    print("*-" * 60)

    t0 = time.time()
    for ep in range(1, stage2_episodes + 1):
        score, tile, crossed = run_episode_stage(agent, target_stage=2, alpha=alpha, rng=rng)
        history["s2_scores"].append(score)
        history["s2_tiles"].append(tile)

        if ep % eval_every == 0:
            elapsed  = time.time() - t0
            roll  = np.mean(history["s2_scores"][-eval_every:])
            best  = max(history["s2_tiles"][-eval_every:])
            cross_pct = 100 * np.mean([t >= boundary for t in history["s2_tiles"][-eval_every:]])
            print(
                f"[S2] ep {ep:>6,} |"
                f"avg {roll:>8,.0f} |"
                f"best {best:>5} |"
                f"reach S2: {cross_pct:4.1f}% |"
                f"{ep/elapsed:>4.0f} ep/s"
            )

        if checkpoint_every > 0 and ep % checkpoint_every == 0:
            agent.save(f"{checkpoint_prefix}_after_s2_ep{ep}")

    print(f"\nStage 2 training done in {(time.time()-t0)/60:.1f} min")
    print(f"Stage 2 table coverage: {agent.nets[2].nonzero_ratio():.1%}\n")

    #  Phase 2: Train Stage 1 
    print("*-" * 80)
    print(f"Phase 2: Training Stage 1 (max tile < {boundary})")
    print(f"Stage 2 network is FROZEN — used as bootstrap oracle")
    print(f" {stage1_episodes:,} episodes, alpha={alpha}")
    print("*-" * 80)

    t0 = time.time()
    for ep in range(1, stage1_episodes + 1):
        score, tile, crossed = run_episode_stage(agent, target_stage=1, alpha=alpha, rng=rng)
        history["s1_scores"].append(score)
        history["s1_tiles"].append(tile)

        if ep % eval_every == 0:
            # Full evaluation using both networks together
            e_scores, e_tiles = evaluate_ms(agent, eval_games, rng=rng)
            history["eval_scores"].append(float(np.mean(e_scores)))
            history["eval_tiles"].append(float(np.mean(e_tiles)))
            history["eval_at"].append(ep)

            elapsed  = time.time() - t0
            win_pct  = 100 * np.mean([t >= 2048 for t in e_tiles])
            roll     = np.mean(history["s1_scores"][-eval_every:])
            best     = max(history["s1_tiles"][-eval_every:])

            print(
                f"[S1] ep {ep:>6,} | "
                f"training score {roll:>8,.0f} | "
                f"evaluation score {np.mean(e_scores):>8,.0f} | "
                f">=2048: {win_pct:4.1f}% | "
                f"best: {best:>5} | "
                f"{ep/elapsed:>4.0f} ep/s"
            )

        if checkpoint_every > 0 and ep % checkpoint_every == 0:
            agent.save(f"{checkpoint_prefix}_after_s1_ep{ep}")

    print(f"\nStage 1 training done in {(time.time()-t0)/60:.1f} min")
    print(f"Stage 1 table coverage: {agent.nets[1].nonzero_ratio():.1%}")

    return agent, history


#MULTISTAGE THIS MOFO

def evaluate_ms( agent:MultiStageAgent, episodes: int = 1_000,
    rng:Optional[np.random.Generator] = None,seed:int = 811,) -> Tuple[List[int], List[int]]:
    """
    Evaluate the multi-stage agent (no learning, both networks active).
    Returns (scores, max_tiles).
    """
    if rng is None:
        rng = np.random.default_rng(seed)

    scores, tiles = [], []
    for ep in range(episodes):
        board = add_random_tile(add_random_tile(new_board(), rng), rng)
        total_score = 0

        while not is_terminal(board):
            direction, afterstate, score = select_move_ms(board, agent)
            total_score += score
            board = add_random_tile(afterstate, rng)

        scores.append(total_score)
        tiles.append(max_tile(board))

    return scores, tiles



if __name__ == "__main__":
    agent, history = train_multistage(stage2_episodes= 30_000, stage1_episodes= 30_000, alpha            = 0.1,
    eval_every= 1_000,eval_games = 200, checkpoint_every = 10_000, checkpoint_prefix= "ms",
        seed = 811, )
    agent.save("ms_final")
    print("\nFinal evaluation — Multi-stage agent (1,000 games):")
    scores, tiles = evaluate_ms(agent, 1_000)
    print(report(scores, tiles, "Multi-stage TD"))
