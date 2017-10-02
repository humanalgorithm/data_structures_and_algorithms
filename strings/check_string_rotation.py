'''
Checks to see if one string is a substring of anoter. Algorithm should check whether
that string is a match both forwards and backwards wrapping around the array
when nessecary.
'''

string1 = "waterbottle"
substring1 = "bottlewater"
substring2 = "elttobretaw"

substring3 = "botisnotwater"
substring4 = "elttibretaw"


def check_is_substring(str1, str2):
    def check_forwards():
        match = True
        for i in range(0, len(str1)):
            str2_position = (j+i)%len(str2)
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
            str2_position = (j-i)%len(str2)
            if str2[str2_position] == str1[i]:
                pass
            else:
                match = False
                break
        if match == True:
            return True

    for j in range(0, len(str2)):
        if str2[j] == str1[0]:
            forward_result, backward_result = check_forwards(),check_backwards()
            if forward_result or backward_result:
                return True
    return False

result = check_is_substring(string1, substring1)
print "checking to see if " + substring1 + " is a substring of " + string1
print "result is - ", result

result = check_is_substring(string1, substring2)
print "checking to see if " + substring2 + " is a substring of " + string1
print "result is - ", result

result = check_is_substring(string1, substring3)
print "checking to see if " + substring3 + " is a substring of " + string1
print "result is - ", result

result = check_is_substring(string1, substring4)
print "checking to see if " + substring4 + " is a substring of " + string1
print "result is - ", result



