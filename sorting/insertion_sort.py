"""
Insertion is an O(n^2) sorting algorithm by by splitting the array into a sorted side and a unsorted side. On
each iteration of the sort it will take an element from the unsorted side and put it into its correct position in
the sorted side. On each iteration we move the sorted index up by 1. One advantage of insertion sort over bubble
sort is that if the next element in the unsorted array is already sorted then we don't need to loop through he entire
list, we only  need to compare the last element in the sorted array to first element in the unsorted array.
"""

from . import print_description, SetupDemo


class InsertionSort(object):
    def insertion_sort(self, dataset):
        for sorted_index in range(1, len(dataset)):
            j = sorted_index
            while j >= 1 and dataset[j] < dataset[j - 1]:
                temp = dataset[j - 1]
                dataset[j - 1] = dataset[j]
                dataset[j] = temp
                j = j - 1
        return dataset


class InsertionSortDemo(SetupDemo):
    def __init__(self):
        super(InsertionSortDemo, self).setup_demo(__file__)
        self.data_set1 = [2, 6, 8, 2, 3, 787, 23, 4, 66, 33, 99, 345, 34, 2324, 4567, 32, 5, 57, 324, 44, 2, 3, 3, 32,
                          32, 456]
        self.data_set2 = [1, 1, 1, 34, 2345, 257, 8, 1, 89, 1, 6234, 56, 2, 45, 2323, 54, 8, 2, 344, 88, 435, 8337, 82,
                          3, 2, 9, 7]
        self.data_set_small = [9, 6, 8, 2, 4]

    def _log_data_before_start(self, data_set):
        message = "Data before sort is "
        print "{} data={}".format(message, data_set)

    def _log_result(self, result):
        print "Result of sort --> "
        print result

    def _run_insertion_sort(self, data_set):
        insertion_sort = InsertionSort()
        self._log_data_before_start(data_set)
        result = insertion_sort.insertion_sort(dataset=data_set)
        self._log_result(result)

    @print_description
    def sort_data_set1(self):
        self._run_insertion_sort(data_set=self.data_set1)

    @print_description
    def sort_data_set2(self):
        self._run_insertion_sort(data_set=self.data_set2)

    @print_description
    def sort_data_set_small(self):
        self._run_insertion_sort(data_set=self.data_set_small)

if __name__ == "__main__":
    is_demo = InsertionSortDemo()
    demos_to_run = [is_demo.sort_data_set1, is_demo.sort_data_set2, is_demo.sort_data_set_small]
    [func() for func in demos_to_run]
