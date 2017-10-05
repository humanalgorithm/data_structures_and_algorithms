'''

'''
from . import print_description, SetupDemo

class Fibonacci(object):

    def log_recursive_array_progress(sef, array):
        print "current fib array --> ", str(array)

    def log_recursive_calcualtion_progress(self, position, fib_minus_one, fib_minus_two):
        print "At position: " + str(position) + " adding fib-1=" + str(fib_minus_one) + \
              " + fib-2=" + str(fib_minus_two) + " to get result --> " + str(fib_minus_one + fib_minus_two)

    def log_loop_progress(self, fib_array, index):
        print "Result=" + str(fib_array[index]) +  " at index=" +  str(index+1) + \
              " as a result of adding index " + str(index) + "=" + str(fib_array[index - 1]) + \
              " + " + "index " + str(index-1) + "=" + str(fib_array[index - 2])\

    def fibonacci_recursive_array(self, target, current=2, fibonacci_array=[1, 1], log=False):
        if log: self.log_recursive_array_progress(fibonacci_array)
        if current == target:
            return fibonacci_array
        next = fibonacci_array[current-1] + fibonacci_array[current-2]  #get last 2 elements
        fibonacci_array.append(next)

        return self.fibonacci_recursive_array(target, current + 1, fibonacci_array, log)

    def fibonacci_at_position_recursive_calculation(self, position, log=False):
        if position == 1:
            return 1
        elif position == 0:
            return 1
        else:
            fib_minus_one = self.fibonacci_at_position_recursive_calculation(position-1, log)
            fib_minus_two = self.fibonacci_at_position_recursive_calculation(position-2, log)
            if log: self.log_recursive_calcualtion_progress(position, fib_minus_one, fib_minus_two)
            return fib_minus_one + fib_minus_two

    def fibonacci_using_loop(self, target_index, log=False):
        fib_array = [1, 1]
        for i in range(2, target_index):
            fib_array.append(fib_array[i-1] + fib_array[i-2])
            if log: self.log_loop_progress(fib_array, i)


class FibonacciDemo(SetupDemo):
    def __init__(self):
        super(FibonacciDemo, self).setup_demo(__file__)

    @print_description
    def fibonacci_at_position_recursive_calculation_9th_item(self):
        Fibonacci().fibonacci_at_position_recursive_calculation(9, log=True)

    @print_description
    def fibonacci_using_loop_7th_item(self):
        Fibonacci().fibonacci_using_loop(7, log=True)

    @print_description
    def fibonacci_recursive_array_5th_item(self):
        Fibonacci().fibonacci_recursive_array(target=5, log=True)

if __name__ == "__main__":
    fib_demo = FibonacciDemo()
    demos_to_run = [fib_demo.fibonacci_at_position_recursive_calculation_9th_element,
                    fib_demo.fibonacci_using_loop_7th_element,
                    fib_demo.fibonacci_recursive_array_5th_element]
    [func() for func in demos_to_run]