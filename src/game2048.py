import random
import numpy as np
from typing import Optional, Tuple, List


board_length = 4
board_size  = board_length **2   # 16

left  = 0
up = 1
right = 2
down  = 3
direction_names = {left: "LEFT", up: "UP", right: "RIGHT", down: "DOWN"}

tile_2_prob = 0.9
tile_4_prob = 0.1
max_tile_exp = 15  # tile 11 is 2048



def _compress(mat: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """Pack all non-zero tiles to the left of each row."""
    changed = False
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed


def _merge(mat: List[List[int]]) -> Tuple[List[List[int]], bool, int]:
  
    changed = False
    score = 0
    for i in range(4):
        for j in range(3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j + 1]:
                mat[i][j]*= 2
                mat[i][j + 1] = 0
                score += mat[i][j]
                changed = True
    return mat, changed, score


def _reverse(mat: List[List[int]]) -> List[List[int]]:
    """Flip each row horizontally."""
    return [row[::-1] for row in mat]


def _transpose(mat: List[List[int]]) -> List[List[int]]:
    """Swap rows and columns (matrix transpose)."""
    return [[mat[j][i] for j in range(4)] for i in range(4)]


def _move_left(grid: List[List[int]]) -> Tuple[List[List[int]], bool, int]:
    """Slide all tiles left. Returns (new_grid, changed, score)."""
    g,c1 = _compress(grid)
    g, c2, score = _merge(g)
    g, _ = _compress(g) # compact again after merges clear gaps
    return g, (c1 or c2), score


def _move_right(grid: List[List[int]]) -> Tuple[List[List[int]], bool, int]:
    g, changed, score = _move_left(_reverse(grid))
    return _reverse(g), changed, score


def _move_up(grid: List[List[int]]) -> Tuple[List[List[int]], bool, int]:
    g, changed, score = _move_left(_transpose(grid))
    return _transpose(g), changed, score


def _move_down(grid: List[List[int]]) -> Tuple[List[List[int]], bool, int]:
    g, changed, score = _move_right(_transpose(grid))
    return _transpose(g), changed, score


_MOVE_FN = {
    left:_move_left,
    right: _move_right,
    up:_move_up,
    down:_move_down,
}

def _find_empty(mat: List[List[int]]) -> Optional[Tuple[int, int]]:
    """Return (row, col) of the first empty cell, or None if full."""
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return i, j
    return None

def _add_new_tile(mat: List[List[int]]) -> None:
    """
    Place a 2 (90%) or 4 (10%) on a random empty cell
    """
    if all(mat[i][j] != 0 for i in range(4) for j in range(4)):
        return

    tile = 2 if (random.random() < tile_2_prob) else 4
    for _ in range(30):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = tile
            return

    cell = _find_empty(mat)
    if cell is not None:
        mat[cell[0]][cell[1]] = tile


def _get_current_state(mat: List[List[int]]) -> str:
    """
    Return one of: 'WON', 'GAME NOT OVER', 'LOST'.
    """
  

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'

    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'

    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'

    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'



def _mat_to_board(mat: List[List[int]]) -> np.ndarray:
    """Convert list-of-lists of tile values -> flat exponent array."""
    board = np.zeros(board_size, dtype=np.uint8)
    for i in range(4):
        for j in range(4):
            v = mat[i][j]
            if v > 0:
                board[i * 4 + j] = int(np.log2(v))
    return board


def _board_to_mat(board: np.ndarray) -> List[List[int]]:
    """Convert flat exponent array -> list-of-lists of tile values."""
    mat = []
    for i in range(4):
        row = []
        for j in range(4):
            exp = int(board[i * 4 + j])
            row.append(0 if exp == 0 else int(1 << exp))
        mat.append(row)
    return mat




def new_board() -> np.ndarray:
    """Return a fresh empty board as array."""
    return np.zeros(board_size, dtype=np.uint8)


def board_from_2d(grid: List[List[int]]) -> np.ndarray:
    """
    Convert a 4x4 list-of-lists of actual tile values into the internal
    exponent representation used by the n-tuple network.

    """
    return _mat_to_board(grid)


def board_to_2d(board: np.ndarray) -> List[List[int]]:
    """Convert exponent board back to actual tile values."""
    return _board_to_mat(board)


def max_tile(board: np.ndarray) -> int:
    """Return the actual value of the highest tile (e.g. 2048)."""
    exp = int(board.max())
    return 0 if exp == 0 else int(1 << exp)


def max_tile_exp(board: np.ndarray) -> int:
    """Return the exponent of the highest tile (e.g. 11 for 2048)."""
    return int(board.max())



def apply_move(board: np.ndarray, direction: int) -> Tuple[np.ndarray, int, bool]:
  
    mat= _board_to_mat(board)
    new_mat, changed, score = _MOVE_FN[direction](mat)
    afterstate = _mat_to_board(new_mat)
    return afterstate, int(score), changed


def get_afterstate(board: np.ndarray, direction: int) -> Tuple[Optional[np.ndarray], int]:
    """
    Return (afterstate, score), or (None, 0) if the move is invalid.
    """
    afterstate, score, changed = apply_move(board, direction)
    if not changed:
        return None, 0
    return afterstate, score


def get_empty_cells(board: np.ndarray) -> np.ndarray:
    """Return flat indices of all empty (zero) cells."""
    return np.where(board == 0)[0]


def add_random_tile(board: np.ndarray, rng: Optional[np.random.Generator] = None) -> np.ndarray:
    """
    Spawn a 2 (90%) or 4 (10%) on a random empty cell.
    Returns a NEW board; does not modify in place.
    """
    mat= _board_to_mat(board)
    new_mat = [row[:] for row in mat]
    _add_new_tile(new_mat)
    return _mat_to_board(new_mat)


def spawn_probability(board: np.ndarray) -> List[Tuple[np.ndarray, float]]:
 
    empty = get_empty_cells(board)
    if len(empty) == 0:
        return []

    p_per_cell = 1.0 / len(empty)
    results= []
    for cell in empty:
        for tile_exp, tile_prob in [(1, tile_2_prob), (2, tile_4_prob)]:
            new_b= board.copy()
            new_b[cell] = tile_exp
            results.append((new_b, p_per_cell * tile_prob))
    return results



def is_terminal(board: np.ndarray) -> bool:
    """Return True if no valid moves exist (game WON or LOST)."""
    return _get_current_state(_board_to_mat(board)) in ('WON', 'LOST')


def get_valid_moves(board: np.ndarray) -> List[int]:
    """Return list of valid move direction constants."""
    valid = []
    for direction in [left, up, right, down]:
        _, _, changed = apply_move(board, direction)
        if changed:
            valid.append(direction)
    return valid


def get_game_status(board: np.ndarray) -> str:
    """Return 'WON', 'GAME NOT OVER', or 'LOST'."""
    return _get_current_state(_board_to_mat(board))



def _flip_board_h(board: np.ndarray) -> np.ndarray:
    """Flip board horizontally (left <-> right)."""
    return board.reshape(4, 4)[:, ::-1].flatten()


def _rotate_board_90(board: np.ndarray) -> np.ndarray:
    """Rotate board 90 degrees clockwise."""
    return board.reshape(4, 4).T[:, ::-1].flatten()


def get_symmetries(board: np.ndarray) -> List[np.ndarray]:
  
    symmetries = []
    b = board.copy()
    for _ in range(4):
        symmetries.append(b.copy())
        symmetries.append(_flip_board_h(b))
        b = _rotate_board_90(b)
    return symmetries



def run_game(policy,rng: Optional[np.random.Generator] = None,max_moves: int = 100_000,) -> Tuple[int, int, List[int]]:

    if rng is not None:
        random.seed(int(rng.integers(0, 2**31)))

    mat = [[0] * 4 for _ in range(4)]
    _add_new_tile(mat)
    _add_new_tile(mat)
    board = _mat_to_board(mat)

    total_score: int= 0
    tile_history: List[int] = []

    for _ in range(max_moves):
        if is_terminal(board):
            break

        direction = policy(board)
        afterstate, score, changed = apply_move(board, direction)

        if not changed:
            valid = get_valid_moves(board)
            if not valid:
                break
            direction= valid[0]
            afterstate, score, _ = apply_move(board, direction)

        total_score += score
        board= add_random_tile(afterstate, rng)
        tile_history.append(max_tile(board))

    return total_score, max_tile(board), tile_history



def start_game() -> List[List[int]]:
    """Initialise a new game matrix and print the control instructions."""
    mat = [[0] * 4 for _ in range(4)]
    print("Commands are as follows:")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    _add_new_tile(mat)
    return mat


def play_interactive():
    """
    Terminal game loop for human play.
    Useful for smoke-testing the move logic by hand.
    """
    mat   = start_game()
    score = 0
    _add_new_tile(mat)   # second starting tile

    key_map = {'w': up, 's': down, 'a': left, 'd': right}

    while True:
        print_board(_mat_to_board(mat))
        print(f"Score: {score}")
        status = _get_current_state(mat)
        if status == 'WON':
            print("You reached 2048 - You WON!")
            break
        if status == 'LOST':
            print("No moves left - GAME OVER.")
            break

        key = input("Move (w/a/s/d): ").strip().lower()
        if key not in key_map:
            print("Unknown key, try w/a/s/d.")
            continue

        direction = key_map[key]
        new_mat, changed, move_score = _MOVE_FN[direction](mat)
        if not changed:
            print("That move doesn't change the board, try another.")
            continue

        mat = new_mat
        score += move_score
        _add_new_tile(mat)




def render_board(board: np.ndarray) -> str:
    """Return a formatted string showing actual tile values."""
    grid  = board_to_2d(board)
    sep   = "+--------+--------+--------+--------+"
    lines = [sep]
    for row in grid:
        cells = "|".join(f"{(v if v > 0 else ''):^8}" for v in row)
        lines.append(f"|{cells}|")
        lines.append(sep)
    return "\n".join(lines)


def print_board(board: np.ndarray) -> None:
    print(render_board(board))