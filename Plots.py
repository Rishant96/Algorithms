import matplotlib.pyplot as plt

sizes = [2500, 5000, 7500, 10000]

bubble_avg = [0.484375, 2.140625, 4.40625, 7.515625]
bubble_best = [0.234375, 0.953125, 2.28125, 3.703125]
bubble_worst = [0.65625, 2.796875, 6.203125, 10.6875]

insertion_avg = [0.20625, 0.871875, 1.959375, 3.8625]
insertion_best = [0.0, 0.003125, 0.003125, 0.00625]
insertion_worst = [0.40625, 1.6625, 3.68125, 7.575]

selection_avg = [0.153125, 0.703125, 1.696875, 2.953125]
selection_best = [0.171875, 0.7125, 1.703125, 2.76875]
selection_worst = [0.19375, 0.69375, 1.671875, 2.99375]

merge_avg = [0.009375, 0.021875, 0.0375, 0.04375]
merge_best = [0.00625, 0.015625, 0.025, 0.034375]
merge_worst = [0.00625, 0.015625, 0.021875, 0.034375]

plt.plot(sizes, bubble_avg)
plt.plot(sizes, insertion_avg)
plt.plot(sizes, selection_avg)
plt.plot(sizes, merge_avg)
plt.legend(['Bubble sort', 'Insertion sort', 'Selection sort', 'Merge Sort'], loc='upper left')
plt.title('Time Complexity Comparison - Average Case')
plt.xlabel('Size of input array')
plt.ylabel('Time (in seconds)')
plt.savefig('plot_average_case.png')
plt.show()

plt.plot(sizes, bubble_best)
plt.plot(sizes, insertion_best)
plt.plot(sizes, selection_best)
plt.plot(sizes, merge_best)
plt.legend(['Bubble sort', 'Insertion sort', 'Selection sort', 'Merge Sort'], loc='upper left')
plt.title('Time Complexity Comparison - Best Case')
plt.xlabel('Size of input array')
plt.ylabel('Time (in seconds)')
plt.savefig('plot_best_case.png')
plt.show()

plt.plot(sizes, bubble_worst)
plt.plot(sizes, insertion_worst)
plt.plot(sizes, selection_worst)
plt.plot(sizes, merge_worst)
plt.legend(['Bubble sort', 'Insertion sort', 'Selection sort', 'Merge Sort'], loc='upper left')
plt.title('Time Complexity Comparison - Worst Case')
plt.xlabel('Size of input array')
plt.ylabel('Time (in seconds)')
plt.savefig('plot_worst_case.png')
plt.show()
