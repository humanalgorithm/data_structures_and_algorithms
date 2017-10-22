"""
Radix sort works by looking at one significant digit in the elements to be sorted at a time. For example if you
were sorting 103, 10, and 201 radix sort would first only look at the ones digit in each of these numbers and sort
on that, so it would order them as 10, 201, 103. After that it would move into the tens digit and then sort
that first sorted listed by the number in the tens digit.  In order to implement radix sort we need to set up
buckets for each of the digits 0-9 so that we have a place to put these numbers as we move through each significant
digit. (Sidenote, if we wanted to implement radix sort for a different base number we would need different numbered
buckets).
"""
from . import print_description, SetupDemo


class RadixSort(object):
    def _reset_radix_map(self):
        return {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    def radix_sort(self, dataset):
        radix_map = self._reset_radix_map()
        n = 10
        m = 1
        length_longest_num = 0
        while True:
            for element in dataset:
                if len(str(element)) > length_longest_num: length_longest_num = len(str(element))
                mod_value = element % n
                divide_value = mod_value / m
                radix_map[divide_value].append(element)
            dataset = []
            for key in radix_map:
                for element in radix_map[key]:
                    dataset.append(element)

            radix_map = self._reset_radix_map()
            n = n * 10
            m = m * 10
            if len(str(n)) > length_longest_num + 1:
                return dataset


class RadixSortDemo(SetupDemo):
    def __init__(self):
        super(RadixSortDemo, self).setup_demo(__file__)
        self.dataset1 = [1, 9, 100, 34, 23, 11, 66, 77, 5, 8, 199]
        self.dataset2 = [201, 1000, 3000, 2000, 5, 6, 3, 10001]
        self.dataset3 = [5, 6, 7, 2, 2, 3, 7, 0, 0, 0, 1, 1, 5]

    @print_description
    def sort_dataset_1(self):
        radix_sort = RadixSort()
        result = radix_sort.radix_sort(self.dataset1)
        print result

    @print_description
    def sort_dataset_2(self):
        radix_sort = RadixSort()
        result = radix_sort.radix_sort(self.dataset2)
        print result

    @print_description
    def sort_dataset_3(self):
        radix_sort = RadixSort()
        result = radix_sort.radix_sort(self.dataset3)
        print result


if __name__ == "__main__":
    radix_demo = RadixSortDemo()
    demos_to_run = [radix_demo.sort_dataset_1, radix_demo.sort_dataset_2, radix_demo.sort_dataset_3]
    [func() for func in demos_to_run]
