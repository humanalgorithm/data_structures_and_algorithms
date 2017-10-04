'''
This demo uses binary search to count the number of occurences of an element in a sorted list. This is accomplished
by 1) finding the right most occurrence of the element to search for 2) finding the left most occurrence of the
 element to search for and then computing the difference in indexes.
'''

from . import print_description, SetupDemo

class DirectionalBinarySearch(object):
    def __init__(self, int_list):
        self.int_list = int_list

    def count_number_of_occurrences(self, search_number):
        left_most_occurrence = self.directional_binary_search(search_number, "left")
        right_most_occurrence = self.directional_binary_search(search_number, "right")
        num_occurrences = right_most_occurrence - left_most_occurrence + 1
        return num_occurrences

    def directional_binary_search(self, check, search_direction):
        low = 0
        high = len(self.int_list)-1
        mid = (high + low)/2
        result = -1
        while low <= high:
            mid = (high + low)/2
            if self.int_list[mid] == check:
                if search_direction == "left":
                    result = mid
                    high = mid -1
                elif search_direction == "right":
                    result = mid
                    low = mid + 1
            elif self.int_list[mid] < check:
                low = mid+1
            elif self.int_list[mid] > check:
                high = mid-1
        return result

class DirectionalBinarySearchDemo(SetupDemo):
    def __init__(self):
        super(DirectionalBinarySearchDemo, self).setup_demo(__file__)
        self.int_list_unique_only = [1, 4, 6, 7, 8, 9, 12, 14, 15, 16, 120, 199, 200, 344, 366, 377, 388]
        self.int_list_with_duplicates = [1, 4, 6, 7, 8, 9, 12, 14, 15, 15, 15, 15, 16, 16, 16, 16, 120, 120, 120, 199,
                                         200, 344, 366, 377, 388]

    @print_description
    def count_occurrences_of_15(self):
        search_number = 15
        directional_binary_search = DirectionalBinarySearch(self.int_list_with_duplicates)
        result = directional_binary_search.count_number_of_occurrences(search_number)
        print "result is "
        print result

    @print_description
    def count_occurrences_of_120(self):
        search_number = 120
        directional_binary_search = DirectionalBinarySearch(self.int_list_with_duplicates)
        result = directional_binary_search.count_number_of_occurrences(search_number)
        print "result is "
        print result

    @print_description
    def find_only_one_element(self):
        search_number = 12
        directional_binary_search = DirectionalBinarySearch(self.int_list_unique_only)
        result = directional_binary_search.count_number_of_occurrences(search_number)
        print "result is ", result

dbs_demo = DirectionalBinarySearchDemo()
demos_to_run = [dbs_demo.count_occurrences_of_15, dbs_demo.count_occurrences_of_120, dbs_demo.find_only_one_element]
[func() for func in demos_to_run]