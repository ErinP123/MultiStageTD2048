import matplotlib.pyplot as plt

def ms_td():
    episodes = list(range(1000, 31000, 1000))
    avg_scores_512=[7249, 12020, 12768, 13141, 13586, 14246, 13018, 14460, 13474, 15266, 14532, 15499, 15539, 14697, 15791, 14012, 16815, 15284, 16524, 15707, 15471, 17050, 16659, 15929, 14945, 16591, 15742, 16338, 16701, 16106]
    avg_scores_1024=[4238, 5582, 6630, 6598, 7952, 7950, 8521, 9438, 9763, 9918, 9914, 10620, 9089, 10935, 11131, 11069, 12392, 11773, 12805, 12424, 12128, 13274, 14484, 13669, 12839, 13718, 14358, 13618, 13304, 13896]

    plt.figure(figsize=(10, 5))
    plt.plot(episodes, avg_scores_512, color='steelblue', linewidth=2, label='512')
    plt.plot(episodes, avg_scores_1024, color='orange', linewidth=2, label='1024')

    plt.xlabel('Training Episodes')
    plt.ylabel('Average Evaluation Score (per 1,000 games)')
    plt.title('MS-TD Learning Curve — Stage 2 Training')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('./figs/MultiStageLearningCurve.png', dpi=150)
    plt.show()

def single_td():
    epidsodes = range(2000, 52000, 2000)

    td0_eval = [5541, 6356, 7296, 8220, 9442, 8336, 9707, 11551, 11577, 12809, 14505, 15275, 17001, 19447, 20971, 20898, 21263, 21603, 21392, 23174, 23354, 21720, 23609, 23722, 22862]
    plt.figure(figsize=(10, 5))
    plt.plot(epidsodes, td0_eval, color='steelblue', linewidth=2)

    plt.xlabel('Training Episodes')
    plt.ylabel('Average Evaluation Score (per 1,000 games)')
    plt.title('Single-TD Learning Curve')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('./figs/SingleStageLearningCurve.png', dpi=150)
    plt.show()

ms_td()
single_td()