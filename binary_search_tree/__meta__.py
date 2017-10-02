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


binary_search_descriptions ={
    "search_for_4": "Name: Search for 4 \n"
                    "Here we set up a binary search by initializing the following array: \n"
                    "[1, 4, 6, 7, 8, 9, 12, 14, 15, 16, 120, 199, 200, 344, 366, 377, 388] \n"
                    "and then searching for the number 4. \n "
                    "Note that the array  list is sorted, we iteratively split the array in \n"
                    "half to get closer to the element we are looking for. In this case we \n"
                    "end up splitting the array iteratively on the first half of the list ",
    "search_for_388": "Name: Search for 388 \n"
                    "Here we set up a binary search by initializing the following array: \n"
                    "[1, 4, 6, 7, 8, 9, 12, 14, 15, 16, 120, 199, 200, 344, 366, 377, 388] \n"
                    "and then searching for the number 388. \n "
                    "Note that the array  list is sorted, we iteratively split the array in \n"
                    "half to get closer to the element we are looking for. In this case we \n"
                    "end up splitting the array iteratively on the second half of the list ",

    "element_not_found": "Name: Element not found\n"
                         "In this demo we look for a nonexistent element, namely the \n"
                         "number 102 which does not exist in the array we are searching \n"
                         "The array we are searching is \n"
                         "[2, 6, 8, 15, 77, 88, 101]"

}


