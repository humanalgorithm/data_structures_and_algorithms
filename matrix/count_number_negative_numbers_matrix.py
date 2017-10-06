"""
This file demonstrates how to count the number of negative numbers in a matrix with each row being sorted. In
this file we demonstrate three different ways to solve the problem 1) In the naive approach we simply loop through
every element in each row and count the number of negatives but this doesn't take advantage of the fact that the
rows are sorted. 2) We show how you can increase the efficiency by counting backwards from the end of each row, until
you find the highest positive number 3) We do binary search to recursively
split the row in two down to the highest negative element in the row.
"""

import numpy
from . import print_description, SetupDemo


class CountNegativeNumbersMatrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def count_negative_numbers_nested_loop(self):
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        neg_num_count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if self.matrix[i][j] < 0:
                    neg_num_count += 1

        return neg_num_count

    def count_negative_numbers_reverse_scan(self):
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        neg_num_count = 0
        for i in range(0, rows):
            for j in range(cols - 1, -1, -1):
                if self.matrix[i][j] < 0:
                    neg_num_count += 1
                if self.matrix[i][j] > 0:
                    continue
        return neg_num_count

    def count_negative_numbers_binary_search(self):
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        neg_num_count = 0

        def binary_search_for_negative_index(row, low, high, highest_negative=0):
            mid = (high + low) / 2

            if row[high] < 0 and high > highest_negative:
                return high

            if low == high:
                return highest_negative

            highest_negative_low = binary_search_for_negative_index(row, low, mid, highest_negative)
            highest_negative_high = 0
            if row[mid + 1] < 1:
                highest_negative_high = binary_search_for_negative_index(row, mid + 1, high, highest_negative)

            return max(highest_negative_low, highest_negative_high)

        def calculate_number_of_elements_by_index(index, row):
            if index == -1 or index == 0:
                return 0
            return index + 1

        for i in range(0, rows):
            row = self.matrix[i]
            negative_index = binary_search_for_negative_index(row, low=0, high=len(row) - 1)
            neg_num_count += calculate_number_of_elements_by_index(negative_index, row)
        return neg_num_count


class CountNegativeNumbersMatrixDemo(SetupDemo):
    def __init__(self):
        super(CountNegativeNumbersMatrixDemo, self).setup_demo(__file__)
        self.matrix = numpy.array([
            [-3, -2, -1, -1, -1, -2, -3],
            [1, 2, 3, 4, 5, 6, 7],
            [-3, -1, -4, 6, 9, 10, 11],
            [0, 0, 2, 4, 7, 8, 10]], numpy.int32
        )

    @print_description
    def count_negative_numbers_nested_loop(self):
        count_matrix = CountNegativeNumbersMatrix(self.matrix)
        result_slow = count_matrix.count_negative_numbers_nested_loop()
        print "The number of negative numbers in this array using slow method is ", result_slow

    @print_description
    def count_negative_numbers_reverse_scan(self):
        count_matrix = CountNegativeNumbersMatrix(self.matrix)
        result_efficient = count_matrix.count_negative_numbers_reverse_scan()
        print "The number of negative numbers in this array using reverse counting is ", result_efficient

    @print_description
    def count_negative_numbers_binary_search(self):
        count_matrix = CountNegativeNumbersMatrix(self.matrix)
        result_binary_search = count_matrix.count_negative_numbers_binary_search()
        print "The number of negative numbers in this array using binary search is ", result_binary_search


if __name__ == "__main__":
    matrix_demo = CountNegativeNumbersMatrixDemo()
    demos_to_run = [matrix_demo.count_negative_numbers_nested_loop,
                    matrix_demo.count_negative_numbers_reverse_scan,
                    matrix_demo.count_negative_numbers_binary_search]
    [func() for func in demos_to_run]
