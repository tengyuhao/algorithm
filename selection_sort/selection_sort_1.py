"""

"""

mylist = [5, 3, 4, 1, 2]
N = len(mylist)

maxItem = mylist[N-1]
maxIndex = N - 1
print(f"Initial maxITem is {maxItem}")


for index in range(N):
    print(f"mylist{index} is mylist[{mylist[index]}]")
    if mylist[index] > maxItem:
        maxItem = mylist[index]
        maxIndex = index

print(f"Current maxIndex is {maxIndex} the max item is {maxItem}")


