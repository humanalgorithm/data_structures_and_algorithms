import random
import time

word = list("abc")

def permutationsCalc(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        #print "".join(string)
        pass

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutationsCalc(string_copy, step + 1)

def anagrams(wordIn, step=0):

    functionid =random.randrange(1,10000)
    if step == len(wordIn):
        #print "".join(wordIn)
        return
    for x in range(step, len(wordIn)):
        loopid = random.randrange(1,10000)
        wordCopy = [character for character in wordIn]
        #print "entered loop with " + str(wordIn) +  "x is " + str(x) + " step is " + str(step) + " functionid: " + str(functionid) + " loopid: " + str(loopid)
        temp = wordCopy[step]
        wordCopy[step] = wordCopy[x]
        wordCopy[x] = temp
        #print "word copy after swap " + str(wordCopy)
        anagrams(wordCopy, step+1)
       # print "return from all anagrams with x is " + str(x) + " step is " + str(step) + " functionid: " + str(functionid)

def permutations(prestring, poststring):
        if len(poststring) <= 1:  #if we have tried all the combinations of post string
            print ''.join(prestring + poststring) #print the string
            return
        for x in range(0, len(poststring)):
            permutations(prestring + list(poststring[x]), poststring[:x] + poststring[x+1:])


start1 = time.time()
permutations([], word)
end1 = time.time()
print end1-start1

'''
start2 = time.time()
permutationsCalc(word)
end2 = time.time()
print end2-start2
'''