def print_separator():
    print "" * 64
    print ":"* 64
    print "" * 64

dict1 = {"key1": "test", "key2": "every", "key3": "worst","key4": "name", "key5": "game"}
dict2 = {"key1": "checking", "key2": "best", "key3": "foo", "key4": "word", "key5": "less"}
dict3 = {"key1": "award", "key2": "abe", "key3": "pertain", "key4": "lane", "key5": "grain"}

list_of_dicts = []
list_of_dicts.append(dict1)
list_of_dicts.append(dict2)
list_of_dicts.append(dict3)


def demo_lambda_sort_dicts_by_key_using_function():
    description = "Name: Sort Dicts by Key Using Function\n" \
                  "This demo sorts a list of dictionaries by a named key.\n" \
                  "When you have a list of dictionaries you can sort their order \n" \
                  "by a key name if all the dicts have the same key name. \n" + \
                  "We declared the sorted array of dictionaries as follows \n" \
                  "sorted_dicts = sorted(list_of_dicts, key=getvaluenolambda) \n"
    "The getvaluenolambda function returns the value at the key we want \n" \
    "to sort on for each iteration of a dictionary in the list. \n\n"

    def getvaluenolambda(current_dict):
        return current_dict["key1"]

    sorted_dicts = sorted(list_of_dicts, key=getvaluenolambda)

    print_separator()
    print description

    print "List of dicts before sort "
    for dict in list_of_dicts: print sorted(dict.items())
    print "\n List of dicts after sort on key name key1"
    for dict in sorted_dicts: print sorted(dict.items())

def demo_lambda_sort_dicts_by_key_using_lambda():
    description = "Name: Sort Dicts by Key Using Lambda\n" \
                  "This demo sorts a list of dictionaries by a named key.\n" \
                  "When you have a list of dictionaries you can sort their order \n" \
                  "by a key name if all the dicts have the same key name. \n" + \
                  "We declared the sorted array of dictionaries as follows \n" \
                  "sorted_dicts = sorted(list_of_dicts, key=lambda k: k[\"key2\"] \n"
    "The key=lambda k: k[\"key2\"] lambda returns the value at the key we want \n" \
    "to sort on for each iteration of a dictionary in the list. \n\n"

    sorted_dicts = sorted(list_of_dicts, key=lambda k: k["key2"])

    print_separator()
    print description
    print "list of dicts before sort "
    for dict in list_of_dicts: print sorted(dict.items())
    print "\n List of dicts after sort on key name key2"
    for dict in sorted_dicts: print sorted(dict.items())

def demo_lambda_sum():
    description = "Name: Use Lambda to Compute Sums \n" \
                  "Use lambda to create a sum function, takes two arguments x and y \n" \
                  "and then adds them together, as x + y, returns the sum \n" \
                  "sum = lambda x, y: x + y"
    print_separator()
    print description

    sum = lambda x, y:   x + y
    print "sum(1, 2) -->", sum(1,2)
    print "sum(10, 20) -->", sum(10, 20)
    print "sum (99, 1) -->", sum(99, 1)

def demo_lambda_dict_comprehension():
    description = "Name: Use Lambda to Construct a Dictionary \n " \
                  "Uses Lambda to take three arguments x, y, z and then print them out \n" + \
                  'test = lambda x, y, z: "x: " + str(x) + " y: " + str(y) + " z: " + str(z)'
    print_separator()
    print description

    test = lambda x, y, z: "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
    print "test(6, 7, 8) --> ", test(6, 7, 8)


def demo_lambda_map_use():
    description = "Name: Use Lambda Map to Compute a List \n" \
                  "Using map function, we apply a lambda to every element in a list \n" \
                  "and get the resulting list. Here a list of numbers is provided and then \n" \
                  "it is passed to a lambda which calculates a value for every element in the list\n" \
                  "and then returns a new list."

    print_separator()
    print description

    print "num_list = [1, 2, 3, 4., 5, 6, 7, 8, 9, 10]"
    print "double_list = map(lambda x: x*2, num_list)"
    num_list = [1, 2, 3, 4., 5, 6, 7, 8, 9, 10]
    double_list = map(lambda x: x*2, num_list)
    print "double_list --> ", double_list


demos_to_run = [demo_lambda_sum, demo_lambda_dict_comprehension, demo_lambda_map_use,
                demo_lambda_sort_dicts_by_key_using_function, demo_lambda_sort_dicts_by_key_using_lambda]
[func() for func in demos_to_run]