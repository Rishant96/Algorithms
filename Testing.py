from time import thread_time
from copy import deepcopy

from RandomListInput import getList

from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from MergeSort import merge_sort


def test_sort_complexity(base_size=2500, runs=10, iters=4):
    sizes = []
    runtimes_avg = []
    runtimes_best = []
    runtimes_worst = []
    for i in range(iters):
        size = base_size * (i+1)
        sizes.append(size)

        random_list = getList(size)
        best_case = getList(size)
        best_case.sort()
        worst_case = getList(size)
        worst_case.sort(reverse=True)

        algos = [bubble_sort, insertion_sort, selection_sort, merge_sort]

        runtimes_avg_t = []
        runtimes_best_t = []
        runtimes_worst_t = []
        for j, algo in enumerate(algos):
            run_10s_avg = []
            run_10s_best = []
            run_10s_worst = []
            for _ in range(runs):
                old_time = thread_time()
                algo(deepcopy(random_list))
                new_time = thread_time()
                run_10s_avg.append(new_time - old_time)

                old_time = thread_time()
                algo(deepcopy(best_case))
                new_time = thread_time()
                run_10s_best.append(new_time - old_time)

                old_time = thread_time()
                algo(deepcopy(worst_case))
                new_time = thread_time()
                run_10s_worst.append(new_time - old_time)
            runtimes_avg_t.append(sum(run_10s_avg)/len(run_10s_avg))
            runtimes_best_t.append(sum(run_10s_best)/len(run_10s_best))
            runtimes_worst_t.append(sum(run_10s_worst)/len(run_10s_worst))
        runtimes_avg.append(runtimes_avg_t)
        runtimes_best.append(runtimes_best_t)
        runtimes_worst.append(runtimes_worst_t)

    print('Average:', runtimes_avg)
    print('Best:', runtimes_best)
    print('Worst:', runtimes_worst)
    print('Sizes:', sizes)


if __name__ == '__main__':
    print()
    test_sort_complexity()
