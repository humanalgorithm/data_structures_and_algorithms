'''
In this example we remove duplicate characters from an array using an in place
sorting algorithm. Since we complete this in only one loop then the time
complexity is O(n). In remove_duplicates we accopmlish this by sorting the
passed in array, in remove_duplicates_using_string_buffer we use a
string ascii value map to assist in the comparisons.
'''


string_array1 = ['a', 'n', 'c', 'd', 'a', 'a', 'n', 't', 't']
string_array2 = ['d', 'n', 'c', 'd', 'd', 'q', 'o', 'p', 't']
string_array3 = ['d', 'd', 'd', 'd']

def remove_duplicates(str_array):
    if str_array == None:
        return None
    if len(str_array) < 2:
        return None

    buffer_duplicates = 0
    for i in range(buffer_duplicates, len(str_array), +1):
        if i < buffer_duplicates:
            i = buffer_duplicates
        for j in range(i+1, len(str_array), +1):
            if str_array[i] == str_array[j]:
                tmp = str_array[buffer_duplicates]
                str_array[buffer_duplicates] = str_array[j]
                str_array[j] = tmp
                buffer_duplicates = buffer_duplicates+1

    duplicates_array = [str_array[i] for i in range(0, buffer_duplicates)]
    uniques_array = [str_array[i] for i in range(buffer_duplicates, len(str_array))]
    return {"Duplicates": duplicates_array,
            "After remove duplicates": uniques_array}

def remove_duplicates_using_string_buffer(str_array):
    ascii_array = [False for i in range (0, 256)]
    tail = 0
    for i in range(0, len(str_array)):
        if not ascii_array[ord(str_array[i])]:
            str_array[tail] = str_array[i]
            ascii_array[ord(str_array[i])] = True
            tail = tail +1

    non_duplicate_list = [str_array[i] for i in range(0, tail)]
    return non_duplicate_list


result = remove_duplicates(string_array1)
print "Result from remove duplicates in place 1 is ", result

result = remove_duplicates(string_array2)
print "Result from remove duplicates in place 2 is  ", result

result = remove_duplicates(string_array3)
print "Result from remove duplicates in place 3 is ", result


result = remove_duplicates_using_string_buffer(string_array1)
print "Result from remove duplicates using string buffer 1 is ", result

result = remove_duplicates_using_string_buffer(string_array2)
print "Result from remove duplicates using string  buffer 2 is ", result

result = remove_duplicates_using_string_buffer(string_array3)
print "Result from remove duplicates using string  buffer 3 is ", result

