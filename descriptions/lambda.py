LambdaDemo = \
    {
        {
            "demo_lambda_sort_dicts_by_key_using_function":
                {
                    "Title": "Sort Dicts by Key Using Function",
                    "Input Data": "list_of_dicts is a list containing dictionaries",
                    "Description": "This demo sorts a list of dictionaries by a named key When you have a list of "
                                   "dictionaries you can sort their order by a key name if all the dicts have the same key "
                                   "name. We declared the sorted array of dictionaries as follows sorted_dicts = "
                                   "sorted(list_of_dicts, key=getvaluenolambda) The getvaluenolambda function returns the "
                                   "value at the key we want to sort on for each iteration of a dictionary in the list."
                }
        },
        {
            "demo_lambda_sort_dicts_by_key_using_lambda":
                {
                    "Title": "Sort Dicts by Key Using Lambda",
                    "Input Data": "list_of_dicts is a list containing dictionaries",
                    "Description": "This demo sorts a list of dictionaries by a named key. When you have a list of "
                                   "dictionaries you can sort their order by a key name if all the dicts have the same "
                                   "key name. We declared the sorted array of dictionaries as follows "
                                   "sorted_dicts = sorted(list_of_dicts, key=lambda k: k[\"key2\"] "
                                   "The key=lambda k: k[\"key2\"] lambda returns the value at the key we want to sort "
                                   "on for each iteration of a dictionary in the list."
                }
        },
        {
            "demo_lambda_sum":
                {"Title": "Use Lambda to Compute Sums",
                 "Input Data": "Takes arguments x and y as input, we pass in integers",
                 "Description": "Use lambda to create a sum function, takes two arguments x and y and then adds them together,"
                                " as x + y and returns the sum. Sum as defined as sum = lambda x, y: x + y"
                 },
        },
        {
            "demo_lambda_dict_comprehension":
                {"Title": "Use Lambda to Construct a Dictionary",
                 "Input Data": "Takes in 3 parameters x, y and z. we pass in 6, 7 and 8",
                 "Description": "Uses Lambda to take three arguments x, y, z and then print them out. "
                                "test = lambda x, y, z: \"x: \" + str(x) + \" y: \" + str(y) + \" z: \" + str(z)",
                 }
        },
        {
            "demo_lambda_map_use":
                {"Title": "Use Lambda Map to Compute a List",
                 "Input Data": "num_list = [1, 2, 3, 4., 5, 6, 7, 8, 9, 10]",
                 "Description": "Using map function, we apply a lambda to every element in a list and get the "
                                "resulting list. Here a list of numbers is provided and then it is passed to a "
                                "lambda which calculates a value for every element in the list and then returns"
                                " a new list."
                 }
        }
    }
