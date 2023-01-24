"""
Selection Sort - Rewrite
"""


def findMaxIndex(mylist, lastIndex):
    maxIndex = lastIndex
    for index in range(lastIndex+1):
        if mylist[index] > mylist[maxIndex]:
            maxIndex = index

    return maxIndex


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


# main program
mylist = [5, 3, 4, 1, 2]


startIndex = len(mylist) - 1
endIndex = 1

for i in range(startIndex, endIndex-1, -1):
    maxindex = findMaxIndex(mylist, i)
    swap(mylist, maxindex, i)

print(mylist)
