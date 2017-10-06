
from . import print_description, SetupDemo

class BubbleSort(object):
    def bubble_sort(self, dataset):
        i = 0
        numPasses = len(dataset)
        sorted = False
        while i < numPasses:
            if sorted == True:
                break
            sorted = True
            j=0
            #last i elements will always be sorted
            while j < len(dataset)-1-i:
                if dataset[j] > dataset[j+1]:
                    temp = dataset[j+1]
                    dataset[j+1] = dataset[j]
                    dataset[j] = temp
                    sorted = False
                j+=1
            i+=1
        return dataset


class BubbleSortDemo(SetupDemo):
    def __init__(self):
        super(BubbleSortDemo, self).setup_demo(__file__)
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

    def _run_bubble_sort(self, data_set):
        bubble_sort = BubbleSort()
        self._log_data_before_start(data_set)
        result = bubble_sort.bubble_sort(dataset=data_set)
        self._log_result(result)

    @print_description
    def sort_data_set1(self):
        self._run_bubble_sort(data_set=self.data_set1)

    @print_description
    def sort_data_set2(self):
        self._run_bubble_sort(data_set=self.data_set2)

    @print_description
    def sort_data_set_small(self):
        self._run_bubble_sort(data_set=self.data_set_small)

bs_demo = BubbleSortDemo()
demos_to_run = [bs_demo.sort_data_set1, bs_demo.sort_data_set2, bs_demo.sort_data_set_small]
[func() for func in demos_to_run]
