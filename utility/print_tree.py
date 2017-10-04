import math


def print_tree_from_breadth_first_stack(stack):
    if stack == None:
        return
    print_space = 64
    num_of_levels = int(math.log(len(stack)+1, 2))

    for level_num in range(1, num_of_levels + 1):
        if level_num == 1:
            num_spaces = (print_space / 2)
            offset = 0
        else:
            math_power = int(math.log(print_space, 2)) - level_num
            num_spaces = (2 ** (math_power))
            offset = int(math.log(print_space, 2))/2*level_num

        start_index = (2 ** (level_num - 1)) - 1
        end_index = start_index + 2 ** (level_num - 1)
        print_str = [" "] * print_space
        for i in range(start_index, end_index):
            elements_at_level = end_index - start_index
            split_level = elements_at_level / 2 + .5
            element_printing_count = (i - start_index) + 1
            if element_printing_count <= split_level:
                index = (element_printing_count * num_spaces) + offset
                print_str[index] = str(stack[i]) if stack[i] else 'x'
            elif element_printing_count >= split_level:
                index = (print_space) - ((elements_at_level + 1 - element_printing_count) * (num_spaces))-offset
                print_str[index] = str(stack[i]) if stack[i] else 'x'
        print ''.join(print_str)
