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



# mylist = [5, 3, 4, 1, 2]
# mylist = [3, 4, 1, 2, 5]
mylist = [3, 2, 1, 4, 5]

# print(findMaxIndex(mylist, 4))
# print(findMaxIndex(mylist, 3))
print(findMaxIndex(mylist, 3-1))