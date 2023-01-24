"""
Insertion Sort
2. Write a program to sort 5 integers in descending order with the insertion sort algorithm. (10')
"""


def insertItem(A, i):
    new_item = A[i]
    j = i - 1

    while j >= 0 and A[j] > new_item:
        A[j + 1] = A[j]
        j = j - 1

    A[j + 1] = new_item


def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        insertItem(A, i)

    return A


# main program
dataset = [104, 99, 102, 41599, 33123]
print(insertionSort(dataset))

# main program
dataset = [44, 22, 66, 33, 99]
print(insertionSort(dataset))


dataset = [11111313223, 1232321, 132323423, 132434, 132434535]
print(insertionSort(dataset))

dataset = [1233, 2, 345, 2245, 1]
print(insertionSort(dataset))


dataset = [2392930203293, 2139231929103, 12213243557656554, 2245, 1]
print(insertionSort(dataset))