
intlistSingle = [1,4,6,7,8,9,12,14,15,16,120,199,200,344,366,377,388]
intlistDoubles = [1,4,6,7,8,9,12,14,15,15,15,15,16,16,16,16,120,120,120,199,200,344,366,377,388]

def binarySearch(listin, check, search):
    low = 0
    high = len(listin)-1
    mid = (high + low)/2
    result = -1
    while low <= high:
        mid = (high + low)/2
        if listin[mid] == check:
            if search == "left":
                result = mid
                high = mid -1
            elif search == "right":
                result = mid
                low = mid + 1
        elif listin[mid] < check:
            low = mid+1
        elif listin[mid] > check:
            high = mid-1
    return result

checkNumber = -2
leftMostOccurence = binarySearch(intlistDoubles, checkNumber, "left")
rightMostOccurence =  binarySearch(intlistDoubles, checkNumber, "right")

numOccurences = rightMostOccurence - leftMostOccurence + 1

print "left Most occurence is " + str(leftMostOccurence) + ", right Most occurence is " + str(rightMostOccurence)
print "Number of occurences of " + str(checkNumber) + " is "  + str(numOccurences)