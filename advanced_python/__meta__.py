import sys

def print_description(f):
    def print_separator():
        print "" * 64
        print ":"* 64
        print "" * 64

    def wrapper(self):
        map_name = self.description_map
        print_separator()
        print getattr(sys.modules[__name__], map_name)[f.__name__]
        f(self)
    return wrapper

lambda_descriptions = {
    "demo_lambda_sort_dicts_by_key_using_function": "Name: Sort Dicts by Key Using Function\n" \
                  "This demo sorts a list of dictionaries by a named key.\n" \
                  "When you have a list of dictionaries you can sort their order \n" \
                  "by a key name if all the dicts have the same key name. \n" + \
                  "We declared the sorted array of dictionaries as follows \n" \
                  "sorted_dicts = sorted(list_of_dicts, key=getvaluenolambda) \n"
    "The getvaluenolambda function returns the value at the key we want \n" \
    "to sort on for each iteration of a dictionary in the list. \n\n",

    "demo_lambda_sort_dicts_by_key_using_lambda": "Name: Sort Dicts by Key Using Lambda\n" \
                  "This demo sorts a list of dictionaries by a named key.\n" \
                  "When you have a list of dictionaries you can sort their order \n" \
                  "by a key name if all the dicts have the same key name. \n" + \
                  "We declared the sorted array of dictionaries as follows \n" \
                  "sorted_dicts = sorted(list_of_dicts, key=lambda k: k[\"key2\"] \n"
    "The key=lambda k: k[\"key2\"] lambda returns the value at the key we want \n" \
    "to sort on for each iteration of a dictionary in the list. \n\n",

    "demo_lambda_sum": "Name: Use Lambda to Compute Sums \n" \
                  "Use lambda to create a sum function, takes two arguments x and y \n" \
                  "and then adds them together, as x + y, returns the sum \n" \
                  "sum = lambda x, y: x + y",

    "demo_lambda_dict_comprehension": "Name: Use Lambda to Construct a Dictionary \n " \
                  "Uses Lambda to take three arguments x, y, z and then print them out \n" + \
                  'test = lambda x, y, z: "x: " + str(x) + " y: " + str(y) + " z: " + str(z)',

    "demo_lambda_map_use": "Name: Use Lambda Map to Compute a List \n" \
                  "Using map function, we apply a lambda to every element in a list \n" \
                  "and get the resulting list. Here a list of numbers is provided and then \n" \
                  "it is passed to a lambda which calculates a value for every element in the list\n" \
                  "and then returns a new list."
}
