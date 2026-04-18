1024

```
Final evaluation (1,000 games):
── TD(0) baseline ── (1000 games)
  Score   mean=    22,526  std=   10,288  max=    67,152
  Tile    mean=     1,531  max= 4,096
  Reach   >=256: 99.7%  >=512: 98.1%  >=1024: 87.5%  >=2048: 54.1%  >=4096:  1.1%
  Distribution:
        64:    2  
       128:    1  
       256:   16  
       512:  106  ████
      1024:  334  █████████████
      2048:  530  █████████████████████
      4096:   11 

```

```
TD(0) baseline | NTupleNetwork(8 tuples × 4 cells, LUT=65,536, mem=2.1 MB)
Training 50,000 episodes, alpha=0.1

  ep   2,000 | train    4,403 | eval    5,541 | >=2048:  0.0% | best:  1024 |     3 ep/s
  ep   4,000 | train    5,848 | eval    6,356 | >=2048:  0.0% | best:  1024 |     3 ep/s
  ep   6,000 | train    6,532 | eval    7,296 | >=2048:  0.0% | best:  1024 |     3 ep/s
  ep   8,000 | train    7,363 | eval    8,220 | >=2048:  0.5% | best:  1024 |     2 ep/s
  ep  10,000 | train    8,064 | eval    9,442 | >=2048:  2.0% | best:  2048 |     2 ep/s
Saved → td0_ep10000.npz
  ep  12,000 | train    8,636 | eval    8,336 | >=2048:  1.0% | best:  2048 |     2 ep/s
  ep  14,000 | train    9,139 | eval    9,707 | >=2048:  2.0% | best:  2048 |     2 ep/s
  ep  16,000 | train   10,130 | eval   11,551 | >=2048:  5.5% | best:  2048 |     2 ep/s
  ep  18,000 | train   11,418 | eval   11,577 | >=2048:  6.5% | best:  2048 |     2 ep/s
  ep  20,000 | train   12,297 | eval   12,809 | >=2048: 15.0% | best:  2048 |     2 ep/s
Saved → td0_ep20000.npz
  ep  22,000 | train   13,208 | eval   14,505 | >=2048: 22.0% | best:  2048 |     2 ep/s
  ep  24,000 | train   14,608 | eval   15,275 | >=2048: 24.5% | best:  2048 |     2 ep/s
  ep  26,000 | train   16,067 | eval   17,001 | >=2048: 35.5% | best:  4096 |     2 ep/s
  ep  28,000 | train   18,496 | eval   19,447 | >=2048: 39.0% | best:  4096 |     2 ep/s
  ep  30,000 | train   19,883 | eval   20,971 | >=2048: 47.5% | best:  4096 |     2 ep/s
Saved → td0_ep30000.npz
  ep  32,000 | train   20,674 | eval   20,898 | >=2048: 48.5% | best:  4096 |     1 ep/s
  ep  34,000 | train   21,196 | eval   21,263 | >=2048: 49.0% | best:  4096 |     1 ep/s
  ep  36,000 | train   22,199 | eval   21,603 | >=2048: 52.5% | best:  4096 |     1 ep/s
  ep  38,000 | train   21,899 | eval   21,392 | >=2048: 48.5% | best:  4096 |     1 ep/s
  ep  40,000 | train   22,618 | eval   23,174 | >=2048: 58.0% | best:  4096 |     1 ep/s
Saved → td0_ep40000.npz
  ep  42,000 | train   22,432 | eval   23,354 | >=2048: 58.0% | best:  4096 |     1 ep/s
  ep  44,000 | train   23,312 | eval   21,720 | >=2048: 54.0% | best:  4096 |     1 ep/s
  ep  46,000 | train   23,411 | eval   23,609 | >=2048: 59.5% | best:  4096 |     1 ep/s
  ep  48,000 | train   22,820 | eval   23,722 | >=2048: 61.5% | best:  4096 |     1 ep/s
  ep  50,000 | train   23,163 | eval   22,862 | >=2048: 57.0% | best:  4096 |     1 ep/s
Saved → td0_ep50000.npz

Done: 50,000 episodes in 711.5 min (1 ep/s)
Table coverage: 33.5% of entries trained
Saved → td0_final.npz
```


```
TD(0) baseline | NTupleNetwork(8 tuples × 4 cells, LUT=65,536, mem=2.1 MB)
Training 50,000 episodes, alpha=0.1

  ep   2,000 | train    3,873 | eval    5,174 | >=2048:  0.0% | best:  1024 |     3 ep/s
  ep   4,000 | train    5,603 | eval    6,032 | >=2048:  0.0% | best:  1024 |     2 ep/s
  ep   6,000 | train    6,367 | eval    6,690 | >=2048:  0.0% | best:  1024 |     2 ep/s
  ep   8,000 | train    7,233 | eval    7,096 | >=2048:  0.0% | best:  1024 |     2 ep/s
  ep  10,000 | train    7,857 | eval    8,185 | >=2048:  0.5% | best:  2048 |     2 ep/s
Saved → td0_ep10000_512.npz
  ep  12,000 | train    8,520 | eval    8,459 | >=2048:  0.5% | best:  2048 |     2 ep/s
  ep  14,000 | train    9,127 | eval    9,221 | >=2048:  1.0% | best:  2048 |     2 ep/s
  ep  16,000 | train    9,882 | eval   10,209 | >=2048:  4.0% | best:  2048 |     2 ep/s
  ep  18,000 | train   10,715 | eval   11,592 | >=2048:  9.0% | best:  2048 |     2 ep/s
  ep  20,000 | train   11,642 | eval   11,991 | >=2048:  7.0% | best:  2048 |     1 ep/s
Saved → td0_ep20000_512.npz
  ep  22,000 | train   12,891 | eval   12,879 | >=2048: 16.0% | best:  2048 |     1 ep/s
  ep  24,000 | train   14,256 | eval   16,328 | >=2048: 29.5% | best:  2048 |     1 ep/s
  ep  26,000 | train   15,606 | eval   16,634 | >=2048: 29.0% | best:  4096 |     1 ep/s
  ep  28,000 | train   16,814 | eval   17,653 | >=2048: 31.5% | best:  4096 |     1 ep/s
  ep  30,000 | train   18,491 | eval   18,929 | >=2048: 34.0% | best:  4096 |     1 ep/s
Saved → td0_ep30000_512.npz
  ep  32,000 | train   20,017 | eval   21,450 | >=2048: 48.0% | best:  4096 |     1 ep/s
  ep  34,000 | train   20,508 | eval   21,673 | >=2048: 50.0% | best:  4096 |     1 ep/s
  ep  36,000 | train   21,125 | eval   20,382 | >=2048: 46.5% | best:  4096 |     1 ep/s
  ep  38,000 | train   21,474 | eval   22,238 | >=2048: 54.5% | best:  4096 |     1 ep/s
  ep  40,000 | train   22,935 | eval   21,508 | >=2048: 51.5% | best:  4096 |     1 ep/s
Saved → td0_ep40000_512.npz
  ep  42,000 | train   22,886 | eval   20,931 | >=2048: 47.0% | best:  4096 |     1 ep/s
  ep  44,000 | train   23,024 | eval   22,563 | >=2048: 53.5% | best:  4096 |     1 ep/s
  ep  46,000 | train   23,298 | eval   24,439 | >=2048: 63.0% | best:  4096 |     1 ep/s
  ep  48,000 | train   22,982 | eval   22,420 | >=2048: 53.5% | best:  4096 |     1 ep/s
  ep  50,000 | train   23,006 | eval   23,106 | >=2048: 54.5% | best:  4096 |     1 ep/s
Saved → td0_ep50000_512.npz

Done: 50,000 episodes in 920.9 min (1 ep/s)
Table coverage: 33.2% of entries trained
Saved → td0_final_512.npz

Final evaluation (1,000 games):
── TD(0) baseline ── (1000 games)
  Score   mean=    23,340  std=   10,667  max=    58,732
  Tile    mean=     1,576  max= 4,096
  Reach   >=256: 99.7%  >=512: 96.7%  >=1024: 86.8%  >=2048: 57.4%  >=4096:  2.0%
  Distribution:
       128:    3  
       256:   30  █
       512:   99  ███
      1024:  294  ███████████
      2048:  554  ██████████████████████
      4096:   20  
```

```
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Phase 1: Training Stage 2 (max tile >= 512)
30,000 episodes, alpha=0.1
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
  [S2] ep  1,000 | avg    2,518 | best  2048 | reach S2: 100.0% |   11 ep/s
  [S2] ep  2,000 | avg    3,398 | best  2048 | reach S2: 100.0% |   10 ep/s
  [S2] ep  3,000 | avg    4,529 | best  2048 | reach S2: 100.0% |    8 ep/s
  [S2] ep  4,000 | avg    5,476 | best  2048 | reach S2: 100.0% |    7 ep/s
  [S2] ep  5,000 | avg    6,512 | best  2048 | reach S2: 100.0% |    6 ep/s
  [S2] ep  6,000 | avg    6,798 | best  2048 | reach S2: 100.0% |    6 ep/s
  [S2] ep  7,000 | avg    6,853 | best  2048 | reach S2: 100.0% |    5 ep/s
  [S2] ep  8,000 | avg    7,146 | best  2048 | reach S2: 100.0% |    5 ep/s
  [S2] ep  9,000 | avg    7,236 | best  2048 | reach S2: 100.0% |    5 ep/s
  [S2] ep 10,000 | avg    7,411 | best  2048 | reach S2: 100.0% |    5 ep/s
Saved → ms_after_s2_ep10000_stage1.npz
Saved → ms_after_s2_ep10000_stage2.npz
  [S2] ep 11,000 | avg    7,699 | best  2048 | reach S2: 100.0% |    5 ep/s
  [S2] ep 12,000 | avg    7,832 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 13,000 | avg    8,009 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 14,000 | avg    7,959 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 15,000 | avg    8,243 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 16,000 | avg    8,477 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 17,000 | avg    8,917 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 18,000 | avg    9,065 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 19,000 | avg    9,746 | best  2048 | reach S2: 100.0% |    4 ep/s
  [S2] ep 20,000 | avg   10,111 | best  4096 | reach S2: 100.0% |    4 ep/s
Saved → ms_after_s2_ep20000_stage1.npz
Saved → ms_after_s2_ep20000_stage2.npz
  [S2] ep 21,000 | avg   10,470 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 22,000 | avg   10,439 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 23,000 | avg   11,144 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 24,000 | avg   11,389 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 25,000 | avg   11,724 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 26,000 | avg   11,386 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 27,000 | avg   12,348 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 28,000 | avg   12,432 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 29,000 | avg   12,288 | best  4096 | reach S2: 100.0% |    3 ep/s
```


```
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Phase 1: Training Stage 2 (max tile >= 512)
30,000 episodes, alpha=0.1
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
  [S2] ep  1,000 | avg    2,224 | best  2048 | reach S2: 100.0% |   12 ep/s
  [S2] ep  2,000 | avg    2,075 | best  2048 | reach S2: 100.0% |   13 ep/s
  [S2] ep  3,000 | avg    3,559 | best  2048 | reach S2: 100.0% |   11 ep/s
  [S2] ep  4,000 | avg    4,502 | best  2048 | reach S2: 100.0% |   10 ep/s
  [S2] ep  5,000 | avg    5,975 | best  2048 | reach S2: 100.0% |    8 ep/s
  [S2] ep  6,000 | avg    6,614 | best  2048 | reach S2: 100.0% |    3 ep/s
  [S2] ep  7,000 | avg    7,261 | best  2048 | reach S2: 100.0% |    3 ep/s
  [S2] ep  8,000 | avg    7,620 | best  2048 | reach S2: 100.0% |    3 ep/s
  [S2] ep  9,000 | avg    8,126 | best  2048 | reach S2: 100.0% |    3 ep/s
  [S2] ep 10,000 | avg    9,004 | best  2048 | reach S2: 100.0% |    3 ep/s
Saved → ms_after_s2_ep10000_stage1.npz
Saved → ms_after_s2_ep10000_stage2.npz
  [S2] ep 11,000 | avg   10,128 | best  4096 | reach S2: 100.0% |    3 ep/s
  [S2] ep 12,000 | avg   11,357 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 13,000 | avg   11,962 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 14,000 | avg   13,298 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 15,000 | avg   13,690 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 16,000 | avg   14,516 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 17,000 | avg   14,860 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 18,000 | avg   15,151 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 19,000 | avg   15,094 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 20,000 | avg   14,792 | best  4096 | reach S2: 100.0% |    2 ep/s
Saved → ms_after_s2_ep20000_stage1.npz
Saved → ms_after_s2_ep20000_stage2.npz
  [S2] ep 21,000 | avg   15,116 | best  4096 | reach S2: 100.0% |    2 ep/s
  [S2] ep 22,000 | avg   14,725 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 23,000 | avg   14,803 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 24,000 | avg   14,330 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 25,000 | avg   14,414 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 26,000 | avg   14,348 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 27,000 | avg   15,096 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 28,000 | avg   14,471 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 29,000 | avg   14,180 | best  4096 | reach S2: 100.0% |    1 ep/s
  [S2] ep 30,000 | avg   13,676 | best  4096 | reach S2: 100.0% |    1 ep/s
Saved → ms_after_s2_ep30000_stage1.npz
Saved → ms_after_s2_ep30000_stage2.npz

Stage 2 training done in 396.8 min
Stage 2 table coverage: 33.9%

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Phase 2: Training Stage 1 (max tile < 512)
Stage 2 network 
 30,000 episodes, alpha=0.1
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
[S1] ep  1,000 | training score    4,367 | evaluation score    7,249 | >=2048:  7.5% | best:  2048 |    3 ep/s
[S1] ep  2,000 | training score    9,240 | evaluation score   12,020 | >=2048: 15.0% | best:  4096 |    3 ep/s
[S1] ep  3,000 | training score   11,246 | evaluation score   12,768 | >=2048: 19.5% | best:  4096 |    2 ep/s
[S1] ep  4,000 | training score   11,393 | evaluation score   13,141 | >=2048: 25.5% | best:  4096 |    2 ep/s
[S1] ep  5,000 | training score   13,234 | evaluation score   13,586 | >=2048: 22.5% | best:  4096 |    2 ep/s
[S1] ep  6,000 | training score   13,348 | evaluation score   14,246 | >=2048: 27.0% | best:  4096 |    2 ep/s
[S1] ep  7,000 | training score   13,621 | evaluation score   13,018 | >=2048: 17.5% | best:  4096 |    2 ep/s
[S1] ep  8,000 | training score   14,329 | evaluation score   14,460 | >=2048: 22.0% | best:  4096 |    2 ep/s
[S1] ep  9,000 | training score   14,604 | evaluation score   13,474 | >=2048: 20.5% | best:  4096 |    2 ep/s
[S1] ep 10,000 | training score   14,867 | evaluation score   15,266 | >=2048: 26.0% | best:  4096 |    2 ep/s
Saved → ms_after_s1_ep10000_stage1.npz
Saved → ms_after_s1_ep10000_stage2.npz
[S1] ep 11,000 | training score   15,307 | evaluation score   14,532 | >=2048: 20.0% | best:  4096 |    2 ep/s
[S1] ep 12,000 | training score   15,426 | evaluation score   15,499 | >=2048: 23.5% | best:  4096 |    1 ep/s
[S1] ep 13,000 | training score   15,052 | evaluation score   15,539 | >=2048: 26.5% | best:  4096 |    1 ep/s
[S1] ep 14,000 | training score   15,671 | evaluation score   14,697 | >=2048: 24.5% | best:  4096 |    1 ep/s
[S1] ep 15,000 | training score   15,873 | evaluation score   15,791 | >=2048: 24.0% | best:  4096 |    1 ep/s
[S1] ep 16,000 | training score   15,971 | evaluation score   14,012 | >=2048: 19.0% | best:  4096 |    1 ep/s
[S1] ep 17,000 | training score   15,818 | evaluation score   16,815 | >=2048: 27.0% | best:  4096 |    1 ep/s
[S1] ep 18,000 | training score   15,976 | evaluation score   15,284 | >=2048: 25.0% | best:  4096 |    1 ep/s
[S1] ep 19,000 | training score   15,917 | evaluation score   16,524 | >=2048: 27.5% | best:  4096 |    1 ep/s
[S1] ep 20,000 | training score   16,178 | evaluation score   15,707 | >=2048: 24.5% | best:  4096 |    1 ep/s
Saved → ms_after_s1_ep20000_stage1.npz
Saved → ms_after_s1_ep20000_stage2.npz
[S1] ep 21,000 | training score   16,311 | evaluation score   15,471 | >=2048: 22.5% | best:  4096 |    1 ep/s
[S1] ep 22,000 | training score   16,400 | evaluation score   17,050 | >=2048: 31.5% | best:  4096 |    1 ep/s
[S1] ep 23,000 | training score   15,545 | evaluation score   16,659 | >=2048: 29.0% | best:  4096 |    1 ep/s
[S1] ep 24,000 | training score   15,886 | evaluation score   15,929 | >=2048: 27.5% | best:  4096 |    1 ep/s
[S1] ep 25,000 | training score   15,305 | evaluation score   14,945 | >=2048: 22.5% | best:  4096 |    1 ep/s
[S1] ep 26,000 | training score   15,998 | evaluation score   16,591 | >=2048: 28.5% | best:  4096 |    1 ep/s
[S1] ep 27,000 | training score   16,436 | evaluation score   15,742 | >=2048: 23.5% | best:  4096 |    1 ep/s
[S1] ep 28,000 | training score   16,057 | evaluation score   16,338 | >=2048: 28.0% | best:  4096 |    1 ep/s
[S1] ep 29,000 | training score   16,120 | evaluation score   16,701 | >=2048: 27.5% | best:  4096 |    1 ep/s
[S1] ep 30,000 | training score   16,919 | evaluation score   16,106 | >=2048: 27.5% | best:  4096 |    1 ep/s
Saved → ms_after_s1_ep30000_stage1.npz
Saved → ms_after_s1_ep30000_stage2.npz

Stage 1 training done in 378.6 min
Stage 1 table coverage: 9.0%
Saved → ms_final_stage1.npz
Saved → ms_final_stage2.npz

Final evaluation — Multi-stage agent (1,000 games):
── Multi-stage TD ── (1000 games)
  Score   mean=    16,108  std=   10,540  max=    59,632
  Tile    mean=     1,095  max= 4,096
  Reach   >=256: 98.9%  >=512: 81.5%  >=1024: 65.1%  >=2048: 28.5%  >=4096:  0.3%
  Distribution:
       128:   11  
       256:  174  ██████
       512:  164  ██████
      1024:  366  ██████████████
      2048:  282  ███████████
      4096:    3  
```

```
Phase 1: Training Stage 2 (max tile >= 1024)
30,000 episodes, alpha=0.1
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
[S2] ep  1,000 |avg    2,424 |best  2048 |reach S2: 100.0% |  11 ep/s
[S2] ep  2,000 |avg    3,225 |best  2048 |reach S2: 100.0% |  11 ep/s
[S2] ep  3,000 |avg    5,008 |best  2048 |reach S2: 100.0% |   9 ep/s
[S2] ep  4,000 |avg    6,048 |best  2048 |reach S2: 100.0% |   7 ep/s
[S2] ep  5,000 |avg    6,537 |best  2048 |reach S2: 100.0% |   6 ep/s
[S2] ep  6,000 |avg    7,201 |best  2048 |reach S2: 100.0% |   6 ep/s
[S2] ep  7,000 |avg    7,942 |best  2048 |reach S2: 100.0% |   5 ep/s
[S2] ep  8,000 |avg    8,741 |best  2048 |reach S2: 100.0% |   2 ep/s
[S2] ep  9,000 |avg    9,583 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 10,000 |avg   10,819 |best  4096 |reach S2: 100.0% |   2 ep/s
Saved → ms_after_s2_ep10000_stage1.npz
Saved → ms_after_s2_ep10000_stage2.npz
[S2] ep 11,000 |avg   11,676 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 12,000 |avg   12,484 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 13,000 |avg   13,042 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 14,000 |avg   13,769 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 15,000 |avg   14,666 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 16,000 |avg   14,504 |best  4096 |reach S2: 100.0% |   2 ep/s
[S2] ep 17,000 |avg   15,211 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 18,000 |avg   14,915 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 19,000 |avg   15,221 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 20,000 |avg   14,810 |best  4096 |reach S2: 100.0% |   1 ep/s
Saved → ms_after_s2_ep20000_stage1.npz
Saved → ms_after_s2_ep20000_stage2.npz
[S2] ep 21,000 |avg   14,812 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 22,000 |avg   14,925 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 23,000 |avg   14,358 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 24,000 |avg   14,147 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 25,000 |avg   14,481 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 26,000 |avg   14,638 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 27,000 |avg   14,346 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 28,000 |avg   14,264 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 29,000 |avg   14,175 |best  4096 |reach S2: 100.0% |   1 ep/s
[S2] ep 30,000 |avg   14,568 |best  4096 |reach S2: 100.0% |   1 ep/s
Saved → ms_after_s2_ep30000_stage1.npz
Saved → ms_after_s2_ep30000_stage2.npz

Stage 2 training done in 385.5 min
Stage 2 table coverage: 33.9%

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Phase 2: Training Stage 1 (max tile < 1024)
Stage 2 network is FROZEN — used as bootstrap oracle
 30,000 episodes, alpha=0.1
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
[S1] ep  1,000 | training score    3,278 | evaluation score    4,238 | >=2048:  0.0% | best:  1024 |    2 ep/s
[S1] ep  2,000 | training score    5,199 | evaluation score    5,582 | >=2048:  1.0% | best:  4096 |    2 ep/s
[S1] ep  3,000 | training score    5,814 | evaluation score    6,630 | >=2048:  3.5% | best:  2048 |    2 ep/s
[S1] ep  4,000 | training score    6,679 | evaluation score    6,598 | >=2048:  5.0% | best:  2048 |    2 ep/s
[S1] ep  5,000 | training score    7,099 | evaluation score    7,952 | >=2048:  5.0% | best:  4096 |    2 ep/s
[S1] ep  6,000 | training score    8,163 | evaluation score    7,950 | >=2048:  5.5% | best:  4096 |    2 ep/s
[S1] ep  7,000 | training score    8,336 | evaluation score    8,521 | >=2048:  5.5% | best:  4096 |    2 ep/s
[S1] ep  8,000 | training score    9,019 | evaluation score    9,438 | >=2048:  9.5% | best:  4096 |    2 ep/s
[S1] ep  9,000 | training score    9,758 | evaluation score    9,763 | >=2048:  7.5% | best:  4096 |    1 ep/s
[S1] ep 10,000 | training score   10,100 | evaluation score    9,918 | >=2048:  9.5% | best:  4096 |    1 ep/s
Saved → ms_after_s1_ep10000_stage1.npz
Saved → ms_after_s1_ep10000_stage2.npz
[S1] ep 11,000 | training score   10,119 | evaluation score    9,914 | >=2048:  8.5% | best:  4096 |    1 ep/s
[S1] ep 12,000 | training score   10,701 | evaluation score   10,620 | >=2048:  9.5% | best:  4096 |    1 ep/s
[S1] ep 13,000 | training score   10,858 | evaluation score    9,089 | >=2048:  7.5% | best:  4096 |    1 ep/s
[S1] ep 14,000 | training score   11,554 | evaluation score   10,935 | >=2048: 11.5% | best:  4096 |    1 ep/s
[S1] ep 15,000 | training score   11,499 | evaluation score   11,131 | >=2048: 13.0% | best:  4096 |    1 ep/s
[S1] ep 16,000 | training score   11,383 | evaluation score   11,069 | >=2048: 11.5% | best:  4096 |    1 ep/s
[S1] ep 17,000 | training score   11,702 | evaluation score   12,392 | >=2048: 14.5% | best:  4096 |    1 ep/s
[S1] ep 18,000 | training score   12,806 | evaluation score   11,773 | >=2048: 11.0% | best:  4096 |    1 ep/s
[S1] ep 19,000 | training score   13,039 | evaluation score   12,805 | >=2048: 16.5% | best:  4096 |    1 ep/s
[S1] ep 20,000 | training score   12,488 | evaluation score   12,424 | >=2048: 13.5% | best:  4096 |    1 ep/s
Saved → ms_after_s1_ep20000_stage1.npz
Saved → ms_after_s1_ep20000_stage2.npz
[S1] ep 21,000 | training score   12,574 | evaluation score   12,128 | >=2048: 14.0% | best:  4096 |    1 ep/s
[S1] ep 22,000 | training score   13,500 | evaluation score   13,274 | >=2048: 18.0% | best:  4096 |    1 ep/s
[S1] ep 23,000 | training score   13,157 | evaluation score   14,484 | >=2048: 24.0% | best:  4096 |    1 ep/s
[S1] ep 24,000 | training score   13,618 | evaluation score   13,669 | >=2048: 19.5% | best:  4096 |    1 ep/s
[S1] ep 25,000 | training score   14,377 | evaluation score   12,839 | >=2048: 16.5% | best:  4096 |    1 ep/s
[S1] ep 26,000 | training score   13,913 | evaluation score   13,718 | >=2048: 19.5% | best:  4096 |    1 ep/s
[S1] ep 27,000 | training score   14,263 | evaluation score   14,358 | >=2048: 20.0% | best:  4096 |    1 ep/s
[S1] ep 28,000 | training score   14,122 | evaluation score   13,618 | >=2048: 17.0% | best:  4096 |    1 ep/s
[S1] ep 29,000 | training score   14,772 | evaluation score   13,304 | >=2048: 16.0% | best:  4096 |    1 ep/s
[S1] ep 30,000 | training score   14,330 | evaluation score   13,896 | >=2048: 19.0% | best:  4096 |    1 ep/s
Saved → ms_after_s1_ep30000_stage1.npz
Saved → ms_after_s1_ep30000_stage2.npz

Stage 1 training done in 432.1 min
Stage 1 table coverage: 14.4%
Saved → ms_final_stage1.npz
Saved → ms_final_stage2.npz

Final evaluation — Multi-stage agent (1,000 games):
── Multi-stage TD ── (1000 games)
  Score   mean=    14,123  std=   10,371  max=    59,336
  Tile    mean=       962  max= 4,096
  Reach   >=256: 99.1%  >=512: 90.2%  >=1024: 51.0%  >=2048: 19.0%  >=4096:  1.0%
  Distribution:
        64:    1  
       128:    8  
       256:   89  ███
       512:  392  ███████████████
      1024:  320  ████████████
      2048:  180  ███████
      4096:   10  
```