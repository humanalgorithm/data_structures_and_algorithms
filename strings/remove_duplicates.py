'''
In this example we remove duplicate characters from an array using an in place
sorting algorithm. Since we complete this in only one loop then the time
complexity is O(n). In remove_duplicates we accopmlish this by sorting the
passed in array, in remove_duplicates_using_string_buffer we use a
string ascii value map to assist in the comparisons.
'''

from . import print_description, SetupDemo

class RemoveDuplicates(object):
    def remove_duplicates_in_place(self, str_array):
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

    def remove_duplicates_using_string_buffer(self, str_array):
        ascii_array = [False for i in range (0, 256)]
        tail = 0
        for i in range(0, len(str_array)):
            if not ascii_array[ord(str_array[i])]:
                str_array[tail] = str_array[i]
                ascii_array[ord(str_array[i])] = True
                tail = tail +1

        non_duplicate_list = [str_array[i] for i in range(0, tail)]
        return non_duplicate_list



class RemoveDuplicatesDemo(SetupDemo):
    def __init__(self):
        super(RemoveDuplicatesDemo, self).setup_demo(__file__)
        self.string_array1 = ['a', 'n', 'c', 'd', 'a', 'a', 'n', 't', 't']
        self.string_array2 = ['d', 'n', 'c', 'd', 'd', 'q', 'o', 'p', 't']
        self.string_array3 = ['d', 'd', 'd', 'd']

    def _log_result_of_removal(self, result):
        print "Result of processing string -->"
        print result

    def _log_string_to_be_processed(self,string):
        message = "String to be processed is -->"
        print "{} string={}".format(message, string)

    def _run_remove_duplicates(self, string_to_process, function_name):
        remove_duplicates = RemoveDuplicates()
        func = getattr(remove_duplicates, function_name)
        self._log_string_to_be_processed(string_to_process)
        result = func(string_to_process)
        self._log_result_of_removal(result)

    @print_description
    def remove_duplicates_in_place_string1(self):
        self._run_remove_duplicates(self.string_array1, "remove_duplicates_in_place")

    @print_description
    def remove_duplicates_in_place_string2(self):
        self._run_remove_duplicates(self.string_array2, function_name="remove_duplicates_in_place")

    @print_description
    def remove_duplicates_in_place_string3(self):
        self._run_remove_duplicates(self.string_array3, function_name="remove_duplicates_in_place")

    @print_description
    def remove_duplicates_using_string_buffer_string1(self):
        self._run_remove_duplicates(self.string_array1, "remove_duplicates_using_string_buffer")

    @print_description
    def remove_duplicates_using_string_buffer_string2(self):
        self._run_remove_duplicates(self.string_array2, "remove_duplicates_using_string_buffer")

    @print_description
    def remove_duplicates_using_string_buffer_string3(self):
        self._run_remove_duplicates(self.string_array3, "remove_duplicates_using_string_buffer")

rd_demo = RemoveDuplicatesDemo()
demos_to_run = [rd_demo.remove_duplicates_in_place_string1, rd_demo.remove_duplicates_in_place_string2,
                rd_demo.remove_duplicates_in_place_string3, rd_demo.remove_duplicates_using_string_buffer_string1,
                rd_demo.remove_duplicates_using_string_buffer_string2, rd_demo.remove_duplicates_using_string_buffer_string3]
[func() for func in demos_to_run]