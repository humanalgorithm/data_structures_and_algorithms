'''
This file sets up a sorted array that we then perform binary search operations on. Binary search is achieved
in an iterative process by using a while loop to iteratively split the list in half until the desired
element is found.
'''
from . import print_description, SetupDemo

class BinarySearch(object):
    def __init__(self, array_list):
        self.array_list = array_list

    def binary_search(self, search_num):
        low = 0
        high = len(self.array_list)-1
        mid = (high + low)/2
        while high-mid !=0:
            mid = (high + low)/2
            if self.array_list[mid] == search_num:
                return mid
            elif self.array_list[mid] < search_num:
                low = mid+1

            elif self.array_list[mid] > search_num:
                high = mid-1
        return -1

class BinarySearchDemo(SetupDemo):
    def __init__(self):
        super(BinarySearchDemo, self).setup_demo(__file__)
        self.__file__ = __file__
        self.int_list_1 = [1, 4, 6, 7, 8, 9, 12, 14, 15, 16, 120, 199, 200, 344, 366, 377, 388]
        self.int_list_2 = [2, 6, 8, 15, 77, 88, 101]

    def _print_found_index(self, index, array_list, *args, **kwargs):
        element = array_list[index]
        tmp = array_list[index]
        if index == -1:
            print "Index was not found in array!"
        else:
            array_list[index] = "FOUND HERE Index=" + str(index) + " element=" + str(array_list[index])
            print array_list
            array_list[index] = tmp

    @print_description
    def search_for_4(self):
        binary_search1 = BinarySearch(self.int_list_1)
        search_for_4 = binary_search1.binary_search(4)
        print "search for element 4 yields index # --> ", search_for_4
        self._print_found_index(search_for_4, self.int_list_1)

    @print_description
    def search_for_388(self):
        binary_search1 = BinarySearch(self.int_list_1)
        search_for_388 = binary_search1.binary_search(388)
        print "search for element 4 yields index # --> ", search_for_388
        self._print_found_index(search_for_388, self.int_list_1)

    @print_description
    def element_not_found(self):
        binary_search1 = BinarySearch(self.int_list_2)
        search_for_102 = binary_search1.binary_search(102)
        print "search for element 102 yields index # --> ", search_for_102
        self._print_found_index(search_for_102, self.int_list_2)

if __name__ == "__main__":
    bst_demo = BinarySearchDemo()
    demos_to_run = [bst_demo.search_for_4, bst_demo.search_for_388, bst_demo.element_not_found]
    [func() for func in demos_to_run]
