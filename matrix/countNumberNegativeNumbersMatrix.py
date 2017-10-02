import numpy

'''
#matrix
[-3, -2, -1, 0, 1, 2 ,3]
[1,  2,  3,  4, 5, 6, 7]
[-3, -1, 4,  6, 9, 10, 11]
[-5,  0, 2,  4, 7, 8,  10]
'''

matrix = numpy.array([
    [-3, -2, -1, -1, -1, -2 ,-3],
    [1,  2,  3,  4, 5, 6, 7],
    [-3, -1, -4,  6, 9, 10, 11],
    [0, 0, 2,  4, 7, 8, 10]], numpy.int32
)

def count_negative_numbers_nm_slow():
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    neg_num_count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] < 0:
                neg_num_count +=1

    return neg_num_count

def count_negative_numbers_efficient():
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    neg_num_count = 0
    for i in range(0, rows):
        for j in range(cols-1, -1, -1):
            if matrix[i][j] < 0:
                neg_num_count +=1
            if matrix[i][j] > 0:
                continue
    return neg_num_count

def count_negative_numbers_binary_search():
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    neg_num_count = 0

    def binary_search_for_negative_index(row, low, high, highest_negative=0):
        mid = (high + low) /2

        if row[high] < 0 and high > highest_negative:
            return high

        if low == high:
            return highest_negative


        highest_negative_low = binary_search_for_negative_index(row, low, mid, highest_negative)
        highest_negative_high = 0
        if row[mid+1] <1:
            highest_negative_high = binary_search_for_negative_index(row, mid+1, high, highest_negative)

        return max(highest_negative_low, highest_negative_high)

    def calculate_number_of_elements_by_index(index, row):
        if index ==-1:
            return 0
        return len(row) -1 - index

    for i in range(0, rows):
        row = matrix[i]
        negative_index = binary_search_for_negative_index(row, low=0, high=len(row)-1)
        neg_num_count += calculate_number_of_elements_by_index(negative_index, row)
    return neg_num_count

result_slow = count_negative_numbers_nm_slow()
result_efficient = count_negative_numbers_efficient()
result_binary_search = count_negative_numbers_binary_search()
print "The number of negative numbers in this array using slow method is ", result_slow
print "The number of negative numbers in this array using reverse counting is ", result_efficient
print "The number of negative numbers in this array using binary search is ", result_efficient
