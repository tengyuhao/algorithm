"""
insertion sort
"""


def insertItem(A, i):
    new_item = A[i]
    j = i - 1

    while j >= 0 and A[j] > new_item:
        A[j + 1] = A[j]
        j = j - 1

    # inserting
    A[j + 1] = new_item


def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        insertItem(A, i)

    return A


# main program
dataset = [5, 2, 1, 4, 3]

print(insertionSort(dataset))