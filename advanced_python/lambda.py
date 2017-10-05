'''
Demonstrates various uses of the lambda function in python. Lambda is a utility that allows you to
construct an anonymous function, which is a function that does not have a name. Lambda is a powerful
tool because you can compute and construct data using fewer lines of code.
'''

from . import print_description, SetupDemo


class LambdaDemo(SetupDemo):
    def __init__(self):
        super(LambdaDemo, self).setup_demo(__file__)
        self.dict1 = {"key1": "test", "key2": "every", "key3": "worst","key4": "name", "key5": "game"}
        self.dict2 = {"key1": "checking", "key2": "best", "key3": "foo", "key4": "word", "key5": "less"}
        self.dict3 = {"key1": "award", "key2": "abe", "key3": "pertain", "key4": "lane", "key5": "grain"}

        self.list_of_dicts = []
        self.list_of_dicts.append(self.dict1)
        self.list_of_dicts.append(self.dict2)
        self.list_of_dicts.append(self.dict3)

    @print_description
    def demo_lambda_sort_dicts_by_key_using_function(self, *args, **kwargs):
        def getvaluenolambda(current_dict):
            return current_dict["key1"]
        sorted_dicts = sorted(self.list_of_dicts, key=getvaluenolambda)
        print "List of dicts before sort "
        for dict in self.list_of_dicts: print sorted(dict.items())
        print "\n List of dicts after sort on key name key1"
        for dict in sorted_dicts: print sorted(dict.items())

    @print_description
    def demo_lambda_sort_dicts_by_key_using_lambda(self, *args, **kwargs):
        sorted_dicts = sorted(self.list_of_dicts, key=lambda k: k["key2"])
        print "list of dicts before sort "
        for dict in self.list_of_dicts: print sorted(dict.items())
        print "\n List of dicts after sort on key name key2"
        for dict in sorted_dicts: print sorted(dict.items())

    @print_description
    def demo_lambda_sum(self, *args, **kwargs):
        sum = lambda x, y:   x + y
        print "sum(1, 2) -->", sum(1,2)
        print "sum(10, 20) -->", sum(10, 20)
        print "sum (99, 1) -->", sum(99, 1)

    @print_description
    def demo_lambda_dict_comprehension(self, *args, **kwargs):
        test = lambda x, y, z: "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
        print "test(6, 7, 8) --> ", test(6, 7, 8)

    @print_description
    def demo_lambda_map_use(self, *args, **kwargs):
        print "num_list = [1, 2, 3, 4., 5, 6, 7, 8, 9, 10]"
        print "double_list = map(lambda x: x*2, num_list)"
        num_list = [1, 2, 3, 4., 5, 6, 7, 8, 9, 10]
        double_list = map(lambda x: x*2, num_list)
        print "double_list --> ", double_list


if __name__ == "__main__":
    lambda_demo = LambdaDemo()
    demos_to_run = [lambda_demo.demo_lambda_sum,
                    lambda_demo.demo_lambda_dict_comprehension,
                    lambda_demo.demo_lambda_map_use,
                    lambda_demo.demo_lambda_sort_dicts_by_key_using_function,
                    lambda_demo.demo_lambda_sort_dicts_by_key_using_lambda]

    [func() for func in demos_to_run]
