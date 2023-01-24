"""
Selection Sort - find max item and max index
"""


def getmin(array, i):

    min = i
    for x in range(i, n):
        if array[x] < array[min]:
            min = x

    return min


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


#
mylist = [5, 3, 4, 1, 2]
n = len(mylist)

startIndex = len(mylist) - 1
endIndex = 1
for i in range(startIndex, endIndex):
    lastindex = i
    # print(i)
    maxindex = getmin(mylist, lastindex)
    swap(mylist, maxindex, lastindex)

print(mylist)
