"""
Selection sort
1. Write a program to sort 5 strings in ascending order with
the selection sort algorithm. (10')
"""


def main(mylist):
    def findMaxIndex(mylist, lastIndex):
        maxIndex = lastIndex
        for index in range(lastIndex + 1):
            if mylist[index] > mylist[maxIndex]:
                maxIndex = index

        return maxIndex

    def swap(a, x, y):
        a[x], a[y] = a[y], a[x]
    startIndex = len(mylist) - 1
    endIndex = 1

    for i in range(startIndex, endIndex-1, -1):
        maxindex = findMaxIndex(mylist, i)
        swap(mylist, maxindex, i)

    return mylist


# main program
L = ["d", "e", "c", "a", "b"]
print(main(L))

L = ["dec", "abc", "efd", "dev", "adf"]
print(main(L))

L = ["efg", "abcd", "abf", "efgd", "xyz"]
print(main(L))

L = ["wyx", "aaa", "xyz", "sdk", "sdkkkk"]
print(main(L))

L = ["vbc", "xds", "xsw", "lwp", "dr"]
print(main(L))

