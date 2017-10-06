'''
A Fibonacci sequence is created by taking the element at position n and calculating it as the sum of the two previous
elements in the sequence before it. An example woudl be 1, 1, 2, 3, 5, 8, 13, 21 ... In this file we show three
different ways to calculate a fibonacci sequence. 1) in a while loop by adding the two previous elements as the current
element 2) by using recursion to build an array and 3) by getting the element at a specified position using
recursion to get the values at n-1 and n-2
'''
from . import print_description, SetupDemo

class Fibonacci(object):

    def fibonacci_recursive_array(self, target, current=2, fibonacci_array=[1, 1], log=lambda x:x):
        log(fibonacci_array)
        if current == target:
            return fibonacci_array
        next = fibonacci_array[current-1] + fibonacci_array[current-2]  #get last 2 elements
        fibonacci_array.append(next)

        return self.fibonacci_recursive_array(target, current + 1, fibonacci_array, log)

    def fibonacci_at_position_recursive_calculation(self, position, log=lambda x,y,z: x):
        if position == 1:
            return 1
        elif position == 0:
            return 1
        else:
            fib_minus_one = self.fibonacci_at_position_recursive_calculation(position-1, log)
            fib_minus_two = self.fibonacci_at_position_recursive_calculation(position-2, log)
            log(position, fib_minus_one, fib_minus_two)
            return fib_minus_one + fib_minus_two

    def fibonacci_using_loop(self, target_index, log=lambda x, y: x):
        fib_array = [1, 1]
        for i in range(2, target_index):
            fib_array.append(fib_array[i-1] + fib_array[i-2])
            log(fib_array, i)


class FibonacciDemo(SetupDemo):
    def __init__(self):
        super(FibonacciDemo, self).setup_demo(__file__)

    def _log_recursive_array_progress(sef, array):
        print "current fib array --> ", str(array)

    def _log_recursive_calculation_progress(self, position, fib_minus_one, fib_minus_two):
        print "At position: " + str(position) + " adding fib-1=" + str(fib_minus_one) + \
              " + fib-2=" + str(fib_minus_two) + " to get result --> " + str(fib_minus_one + fib_minus_two)

    def _log_loop_progress(self, fib_array, index):
        print "Result=" + str(fib_array[index]) + " at index=" +  str(index+1) + \
              " as a result of adding index " + str(index) + "=" + str(fib_array[index - 1]) + \
              " + " + "index " + str(index-1) + "=" + str(fib_array[index - 2])

    @print_description
    def fibonacci_at_position_recursive_calculation_5th_item(self):
        log = self._log_recursive_calculation_progress
        result = Fibonacci().fibonacci_at_position_recursive_calculation(5, log=log)
        print "Result is --> ", result

    @print_description
    def fibonacci_using_loop_7th_item(self):
        log = self._log_loop_progress
        Fibonacci().fibonacci_using_loop(7, log=log)

    @print_description
    def fibonacci_recursive_array_9th_item(self):
        log = self._log_recursive_array_progress
        Fibonacci().fibonacci_recursive_array(target=9, log=log)

if __name__ == "__main__":
    fib_demo = FibonacciDemo()
    demos_to_run = [fib_demo.fibonacci_at_position_recursive_calculation_5th_item,
                    fib_demo.fibonacci_using_loop_7th_item,
                    fib_demo.fibonacci_recursive_array_9th_item]
    [func() for func in demos_to_run]