"""
In this coding problem we take in a string and then print out all of its possible permutations. In this file we
show three different ways to accomplish this 1) anagrams_recursion_on_pre_and_post_string recursively joins a
prestring and poststring in every posssible combination and in 2) anagrams_swap_on_step_and_index we use an inreasing
step that acts as a marker to swap every single element in the array with that step and call itself for each
permutation. 3) anagrams_swap_on_step_and_index_2 works the same but collapses some of the functionality into
fewer lines
"""

from . import SetupDemo, print_description

class AllAnagrams(object):
    def anagrams_swap_on_step_and_index(self, wordIn, step, log=lambda *args, **kwargs: kwargs):
        if step == len(wordIn):
            print "Anagram found: " + "".join(wordIn)
            return
        for x in range(step, len(wordIn)):
            wordCopy = [character for character in wordIn]
            log("loop", x=x, step=step, wordIn=wordIn)
            temp = wordCopy[step]
            wordCopy[step] = wordCopy[x]
            wordCopy[x] = temp
            log("swap", x=x, step=step, wordIn=wordIn, wordCopy=wordCopy)
            self.anagrams_swap_on_step_and_index(wordCopy, step+1, log)
            log("return", x=x, step=step, wordIn=wordIn)

    def anagrams_swap_on_step_and_index_2(self, string, step, log=lambda *args, **kwargs: kwargs):
        # if we've gotten to the end, print the permutation
        if step == len(string):
            print "Anagram found: " + "".join(string)
        # everything to the right of step has not been swapped yet
        for i in range(step, len(string)):
            log("loop", string=string, step=step, i=i)
            # copy the string (store as array)
            string_copy = [character for character in string]
            # swap the current index with the step
            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
            # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
            log("swap", string=string, step=step, i=i, string_copy=string_copy)
            self.anagrams_swap_on_step_and_index_2(string_copy, step + 1, log)
            log("return", string=string, step=step, i=i)

    def anagrams_recursion_on_pre_and_post_string(self, prestring, poststring, log=lambda *args, **kwargs: kwargs):
            if len(poststring) <= 1:  #if we have tried all the combinations of post string
                print ''.join(prestring + poststring) #print the string
                return
            for x in range(0, len(poststring)):
                log(prestring + list(poststring[x]), poststring[:x] + poststring[x+1:], "before")
                self.anagrams_recursion_on_pre_and_post_string(prestring + list(poststring[x]),
                                                               poststring[:x] + poststring[x+1:], log)
                log(prestring + list(poststring[x]), poststring[:x] + poststring[x+1:], "after")

class AllAnagramsDemo(SetupDemo):
    def __init__(self):
        super(AllAnagramsDemo, self).setup_demo(__file__)

    def _log_anagrams_swap_on_step_and_index(self, location, *args, **kwargs):
        if location == "loop":
            print 'message={}, x={}, step={}, wordIn={}'.format("Entered loop", kwargs.get('x'),
                                                                kwargs.get('step'),
                                                                kwargs.get('wordIn'))
        if location == "swap":
            print 'message={}, x={}, step={}, wordIn={}, wordCopy={}'.format("After swap", kwargs.get('x'),
                                                                             kwargs.get('step'),
                                                                             kwargs.get('wordIn'),
                                                                             kwargs.get('wordCopy'))

        if location == "return":
            print 'message={}, x={}, step={}, wordIn={}'.format("After return", kwargs.get('x'),
                                                                kwargs.get('step'),
                                                                kwargs.get('wordIn'))

    def _log_anagrams_swap_on_step_and_index_2(self, location, *args, **kwargs):
        if location == "loop":
            print 'message={}, i={}, step={}, string={}'.format("Entered loop", kwargs.get('i'),
                                                                kwargs.get('step'),
                                                                kwargs.get('string'))
        if location == "swap":
            print 'message={}, i={}, step={}, string={}, string_copy={}'.format("After swap", kwargs.get('i'),
                                                                             kwargs.get('step'),
                                                                             kwargs.get('string'),
                                                                             kwargs.get('string_copy'))

        if location == "return":
            print 'message={}, i={}, step={}, string={}'.format("After return", kwargs.get('i'),
                                                                kwargs.get('step'),
                                                                kwargs.get('string'))

    def _log_pre_post_string(self, prestring, poststring, execution):
        if execution == 'before':
            print "calling anagrams with prestring=" + str(prestring) + " and poststring=" + str(poststring)
        elif execution == "after":
            print "return from all anagrams with prestring=" + str(prestring) + " and poststring=" + str(poststring)

    @print_description
    def anagrams_recursion_on_pre_and_post_string(self):
        all_anagrams = AllAnagrams()
        word = list('abc')
        all_anagrams.anagrams_recursion_on_pre_and_post_string(prestring=[], poststring=word, log=self._log_pre_post_string)

    @print_description
    def anagrams_swap_on_step_and_index(self):
        all_anagrams = AllAnagrams()
        word = list('123')
        all_anagrams.anagrams_swap_on_step_and_index(word, 0, log=self._log_anagrams_swap_on_step_and_index)

    @print_description
    def anagrams_swap_on_step_and_index_2(self):
        all_anagrams = AllAnagrams()
        word = list('123')
        all_anagrams.anagrams_swap_on_step_and_index_2(word, 0, self._log_anagrams_swap_on_step_and_index_2)

if __name__ == "__main__":
    aa_demo = AllAnagramsDemo()
    demos_to_run = [aa_demo.anagrams_recursion_on_pre_and_post_string, aa_demo.anagrams_swap_on_step_and_index,
                    aa_demo.anagrams_swap_on_step_and_index_2]
    [func() for func in demos_to_run]
