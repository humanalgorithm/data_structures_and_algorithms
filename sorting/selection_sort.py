"""
Selection sort is an O(n^2) that works by selecting the lowest element in the array and the moving it to the end of the
sorted portion of the array. At each iteration move the sorted index of the array + , then we loop through the
unsorted portion of the array to find the lowest element and then move it to the end of the sorted portion of the array.
"""

from . import print_description, SetupDemo

class SelectionSort(object):
    def selection_sort(self, data_set):
        for sorted_index in range(0, len(data_set)):
            j = sorted_index + 1
            currentLowElementIndex = sorted_index
            swap = False
            while j < len(data_set):
                if data_set[j] < data_set[currentLowElementIndex]:
                    currentLowElementIndex = j
                    swap = True
                j = j + 1

            if swap:
                temp = data_set[sorted_index]
                data_set[sorted_index] = data_set[currentLowElementIndex]
                data_set[currentLowElementIndex] = temp
        return data_set


class SelectionSortDemo(SetupDemo):
    def __init__(self):
        super(SelectionSortDemo, self).setup_demo(__file__)
        self.data_set1 = [2, 6, 8, 2, 9, 787, 332, 4, 22, 33, 99, 345, 23, 2324, 456, 32, 5, 57, 324, 23, 2, 3, 3, 3,
                          32, 123]
        self.data_set2 = [0, 1, 1, 34, 2345, 257, 8, 1, 732, 1, 6234, 82, 2, 45, 2000, 54, 8, 2, 789, 84, 432, 456, 82,
                          3, 2, 9, 7]
        self.data_set_small = [9, 6, 5, 99, 23]

    def _log_data_before_start(self, data_set):
        message = "Data before sort is "
        print "{} data={}".format(message, data_set)

    def _log_result(self, result):
        print "Result of sort --> "
        print result

    def _run_selection_sort(self, data_set):
        selection_sort = SelectionSort()
        self._log_data_before_start(data_set)
        result = selection_sort.selection_sort(data_set)
        self._log_result(result)

    @print_description
    def sort_data_set1(self):
        self._run_selection_sort(data_set=self.data_set1)

    @print_description
    def sort_data_set2(self):
        self._run_selection_sort(data_set=self.data_set2)

    @print_description
    def sort_data_set_small(self):
        self._run_selection_sort(data_set=self.data_set_small)


ssort_demo = SelectionSortDemo()
demos_to_run = [ssort_demo.sort_data_set1, ssort_demo.sort_data_set2, ssort_demo.sort_data_set_small]
[func() for func in demos_to_run]
