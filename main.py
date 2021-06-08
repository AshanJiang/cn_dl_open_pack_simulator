import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import open_packs


def main():
    packs_num_list = open_packs.open_1000_times()
    arr = np.array(packs_num_list)
    density = stats.gaussian_kde(arr)
    n, x, _ = plt.hist(arr, bins=np.linspace(200, 600, 50), density=True, facecolor='b', alpha=0.75)
    plt.grid(True)
    plt.plot(x, density(x))
    mean = arr.mean()
    std = arr.std()
    plt.text(200, .005, "均值={},标准差={}".format(round(mean, 1), round(std, 1)))
    plt.title("抽1000次的概率分布")
    plt.xlabel("需开包数")
    plt.ylabel("概率")
    plt.show()


if __name__ == '__main__':
    main()
