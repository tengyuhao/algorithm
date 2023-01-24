"""

"""
mylist = [5, 3, 4, 1, 2]


def getmin(array, i):

    min = i
    for x in range(i, len(mylist)):
        if array[x] < array[min]:
            min = x

    return min

print(getmin(mylist, 1))

