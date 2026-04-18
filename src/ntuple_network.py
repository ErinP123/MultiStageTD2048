
import numpy as np
from typing import List
from game2048 import get_symmetries


#  Board layout (flat indices):
#   0  1  2  3
#   4  5  6  7
#   8  9 10 11
#  12 13 14 15

tuples: List[List[int]] = [
    [0,  1,  2,  3],   # row 0
    [4,  5,  6,  7],   # row 1
    [8,  9,  10, 11],  # row 2
    [12, 13, 14, 15],  # row 3
    [0,  4,  8,  12],  # col 0
    [1,  5,  9,  13],  # col 1
    [2,  6,  10, 14],  # col 2
    [3,  7,  11, 15],  # col 3
]

num_exponents = 16  #Exponents
tuple_length  = 4
look_up_table   = num_exponents ** tuple_length   # 16^4 = 65,536



class NTupleNetwork:
    

    def __init__(self):
        # One lookup table per tuple, initialised to zero
        self.luts: List[np.ndarray] = [
            np.zeros(look_up_table, dtype=np.float32) for _ in tuples
        ]

  
    def get_index(self, board, tup):
        idx = 0
        for cell in tup:
            idx = idx * num_exponents + int(board[cell])
        return idx

   
    def evaluate(self, board: np.ndarray) -> float:
        return float(sum(
            lut[self.get_index(board, tup)]
            for lut, tup in zip(self.luts, tuples)))


    def update(self, board: np.ndarray, delta: float, alpha: float) -> None:
   
        step = alpha * delta / 8.0
        for sym in get_symmetries(board):
            for lut, tup in zip(self.luts, tuples):
                lut[self.get_index(sym, tup)] += step

  #https://www.geeksforgeeks.org/python/how-to-save-multiple-numpy-arrays/
    def save(self, path: str) -> None:
        np.savez_compressed(path, *self.luts)
        print(f"Saved → {path}.npz")

    @classmethod
    def load(cls, path: str) -> "NTupleNetwork":
        path = path if path.endswith(".npz") else path + ".npz"
        data = np.load(path)
        net  = cls()
        for i, key in enumerate(sorted(data.files)):
            net.luts[i] = data[key]
        print(f"Loaded {path}")
        return net

    def nonzero_ratio(self) -> float:
        total   = sum(l.size for l in self.luts)
        nonzero = sum(int(np.count_nonzero(l)) for l in self.luts)
        return nonzero / total

    def memory_mb(self) -> float:
        return sum(l.nbytes for l in self.luts) / 1e6

    def __repr__(self) -> str:
        return (f"NTupleNetwork({len(tuples)} tuples "
                f"{tuple_length} cells, "
                f"LUT={look_up_table:,}, "
                f"mem={self.memory_mb():.1f} MB)")
