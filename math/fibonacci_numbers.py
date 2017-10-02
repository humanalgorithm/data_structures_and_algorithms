
# 1, 2, 3, 5, 8, 13, 21

fibarray = [1,2]

'''
for x in range (2, 15):
     toadd =  fibarray[x-1]  + fibarray[x-2]
     fibarray.append(toadd)

print fibarray
'''

def fibonacci(current, target):

    if current == target:
        return
    next = fibarray[current-1] + fibarray[current-2]  #get last 2 elements
    fibarray.append(next)

    fibonacci(current + 1, target)

fibarray = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def fibonaccitest(current):
    global fibarray
    if current == 2:
        return 2
    elif current == 1:
        return 1
    else:
        if fibarray[current-1] == 0:
            fibarray[current-1] = fibonaccitest(current-1) + fibonaccitest(current-2)
            return fibarray[current-1]
        return fibarray[current-1]



def fibonaccitest(current):
    global fibarray
    if current == 1:
        return 1
    elif current == 0:
        return 1
    else:
        fib = fibonaccitest(current-1) + fibonaccitest(current-2)
        print fib
        return fib


print fibonaccitest(90)