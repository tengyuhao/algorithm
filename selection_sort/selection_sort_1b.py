"""
Selection Sort - find max item and max index
"""

mylist = [5, 3, 4, 1, 2]
N = len(mylist)
maxIndex = N-1

for index in range(N):
    if mylist[index] > mylist[maxIndex]:
        maxIndex = index


print(maxIndex, mylist[maxIndex])