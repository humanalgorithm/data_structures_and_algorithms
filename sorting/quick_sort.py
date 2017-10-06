from . import print_description, SetupDemo


class QuickSort(object):

    def quickSort(self, lo, hi, array):
        hi = int(hi)
        lo = int(lo)
        if (hi - lo) < 1:
            return

        j = self.partition(lo, hi, array)
        self.quickSort(lo, j, array)
        self.quickSort(j + 1, hi, array)

        return array

    def partition(self, lo, hi, array):
        i = lo - 1
        j = hi + 1
        pivot = lo
        exit = False

        while exit == False:
            while i <= hi:
                i = i + 1
                if array[i] >= array[pivot]:
                    break

            while j >= lo:
                j = j - 1
                if array[j] <= array[pivot]:
                    if j <= i:
                        exit = True
                        break
                    if i == pivot:
                        pivot = j
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
                    break
        return j


class QuickSortDemo(SetupDemo):
    def __init__(self):
        super(QuickSortDemo, self).setup_demo(__file__)
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

    def _run_quick_sort(self, data_set):
        quick_sort = QuickSort()
        self._log_data_before_start(data_set)
        result = quick_sort.quickSort(lo=0, hi=len(data_set)-1, array=data_set)
        self._log_result(result)

    @print_description
    def sort_data_set1(self):
        self._run_quick_sort(data_set=self.data_set1)

    @print_description
    def sort_data_set2(self):
        self._run_quick_sort(data_set=self.data_set2)

    @print_description
    def sort_data_set_small(self):
        self._run_quick_sort(data_set=self.data_set_small)


qs_demo = QuickSortDemo()
demos_to_run = [qs_demo.sort_data_set1, qs_demo.sort_data_set2, qs_demo.sort_data_set_small]
[func() for func in demos_to_run]
