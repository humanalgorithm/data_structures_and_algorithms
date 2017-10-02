intlistSingle = [1,4,6,7,8,9,12,14,15,16,120,199,200,344,366,377,388]\

def binarySearch(listin, check):
    low = 0
    high = len(listin)
    mid = (high + low)/2
    while high-mid !=0:
        mid = (high + low)/2
        if listin[mid] == check:
            return mid
        elif listin[mid] < check:
            low = mid+1
        elif listin[mid] > check:
            high = mid-1
    return -1

print intlistSingle[(binarySearch(intlistSingle, 4) )]