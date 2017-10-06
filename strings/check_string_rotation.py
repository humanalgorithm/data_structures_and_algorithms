'''
Checks to see if one string is a substring of another. Algorithm should check whether
that string is a match both forwards and backwards wrapping around the array when nessecary.
'''

from . import print_description, SetupDemo

class CheckStringRotation(object):
    def check_is_rotation(self, str1, str2):
        def check_forwards():
            match = True
            for i in range(0, len(str1)):
                str2_position = (j + i) % len(str2)
                if str2[str2_position] == str1[i]:
                    pass
                else:
                    match = False
                    break
            if match == True:
                return True

        def check_backwards():
            match = True
            for i in range(0, len(str1)):
                str2_position = (j - i) % len(str2)
                if str2[str2_position] == str1[i]:
                    pass
                else:
                    match = False
                    break
            if match == True:
                return True

        for j in range(0, len(str2)):
            if str2[j] == str1[0]:
                forward_result, backward_result = check_forwards(), check_backwards()
                if forward_result or backward_result:
                    return True
        return False


class CheckStringRotationDemo(SetupDemo):
    def __init__(self):
        super(CheckStringRotationDemo, self).setup_demo(__file__)

        self.base_string = "waterbottle"
        self.string2 = "bottlewater"
        self.string3 = "bottlewater"

        self.string3 = "elttobretaw"
        self.string4 = "ttobretawel"
        self.string5 = "botisnotwater"
        self.string6 = "elttibretaw"

    def _log_result_of_comparision(self, base_string, compare_string, result):
        message = "Checking to see if string is a rotation of base string -->"
        print message
        print "base string={}, comparision string={}, result={}".format(base_string, compare_string, result)

    @print_description
    def check_string_regular_forwards_match(self):
        check_substring = CheckStringRotation()
        compare_string = self.string2
        result = check_substring.check_is_rotation(self.base_string, compare_string)
        self._log_result_of_comparision(self.base_string, compare_string, result)

    @print_description
    def check_string_forwards_wraparound_match(self):
        check_substring = CheckStringRotation()
        compare_string = self.string3
        result = check_substring.check_is_rotation(self.base_string, compare_string)
        self._log_result_of_comparision(self.base_string, compare_string, result)

    @print_description
    def check_string_backwards_wraparound_match(self):
        check_substring = CheckStringRotation()
        compare_string = self.string4
        result = check_substring.check_is_rotation(self.base_string, compare_string)
        self._log_result_of_comparision(self.base_string, compare_string, result)

    @print_description
    def check_forwards_string_no_match(self):
        check_substring = CheckStringRotation()
        compare_string = self.string5
        result = check_substring.check_is_rotation(self.base_string, compare_string)
        self._log_result_of_comparision(self.base_string, compare_string, result)

    @print_description
    def check_backwards_no_match(self):
        check_substring = CheckStringRotation()
        compare_string = self.string6
        result = check_substring.check_is_rotation(self.base_string, compare_string)
        self._log_result_of_comparision(self.base_string, compare_string, result)


check_string_demo = CheckStringRotationDemo()
demos_to_run = [check_string_demo.check_string_regular_forwards_match,
                check_string_demo.check_string_forwards_wraparound_match,
                check_string_demo.check_string_backwards_wraparound_match,
                check_string_demo.check_forwards_string_no_match,
                check_string_demo.check_backwards_no_match]
[func() for func in demos_to_run]