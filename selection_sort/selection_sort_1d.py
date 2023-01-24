"""
Selection Sort - find max item and max index
"""


def findMaxIndex(mylist, lastIndex):
    # N = len(mylist)
    maxIndex = lastIndex
    for index in range(lastIndex+1):
        if mylist[index] > mylist[maxIndex]:
            maxIndex = index

    return maxIndex


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


mylist = [5, 3, 4, 1, 2]
lastindex = len(mylist)-1
maxindex = findMaxIndex(mylist, lastindex)
swap(mylist, maxindex, lastindex)
print(mylist)
