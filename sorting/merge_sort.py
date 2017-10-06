"""
Merge sort works by breaking the array  into two until there is only one element in each set, then it will then
put together these smaller sets into a larger set recursively until there the entire set is sorted.
"""

from . import print_description, SetupDemo

class MergeSort(object):
    def merge_sort(self, dataset):
        left_array_pass = []
        right_array_pass = []

        lo = 0
        hi = len(dataset) - 1
        mid = (lo + hi) / 2
        i = 0
        r = mid + 1

        while i <= mid:
            left_array_pass.append(dataset[i])
            i = i + 1
        while r <= hi:
            right_array_pass.append(dataset[r])
            r = r + 1

        if (len(dataset)) > 1:
            left_array = self.merge_sort(left_array_pass)
            right_array = self.merge_sort(right_array_pass)
            dataset_merged = self.merge_sets(left_array, right_array)
            return dataset_merged
        else:
            return dataset

    def merge_sets(self, left_array, right_array):
        return_array = []
        i = 0
        j = 0
        k = 0
        return_size = len(left_array) + len(right_array)
        for x in range(0, return_size):
            return_array.append(0)
        while k < return_size:
            if i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    return_array[k] = left_array[i]
                    i += 1
                else:
                    return_array[k] = right_array[j]
                    j += 1
            elif i < len(left_array) and j >= len(right_array):
                return_array[k] = left_array[i]
                i += 1
            elif i >= len(left_array) and j < len(right_array):
                return_array[k] = right_array[j]
                j += 1
            elif i >= len(left_array) and j >= len(right_array):
                break
            k += 1
        return return_array

class MergeSortDemo(SetupDemo):
    def __init__(self):
        super(MergeSortDemo, self).setup_demo(__file__)
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

    def _run_merge_sort(self, data_set):
        merge_sort = MergeSort()
        self._log_data_before_start(data_set)
        result = merge_sort.merge_sort(dataset=data_set)
        self._log_result(result)

    @print_description
    def sort_data_set1(self):
        self._run_merge_sort(data_set=self.data_set1)

    @print_description
    def sort_data_set2(self):
        self._run_merge_sort(data_set=self.data_set2)

    @print_description
    def sort_data_set_small(self):
        self._run_merge_sort(data_set=self.data_set_small)


ms_demo = MergeSortDemo()
demos_to_run = [ms_demo.sort_data_set1, ms_demo.sort_data_set2, ms_demo.sort_data_set_small]
[func() for func in demos_to_run]
