"""
insertion sort
"""


def insertItem(A, i):
    """ insert A[i] into ordered sublist A[0, i-1] """

    # the new item to be inserted with
    new_item = A[i]

    # find the index where the new item should be inserted at
    # 0 <= j <= i-1
    j = i - 1

    # shift compared items to next position to right
    while j >= 0 and A[j] > new_item:
        A[j + 1] = A[j]
        j = j - 1

    # when the loop stopped, the current A[j] is the one
    # which is NOT greater than new_item
    # then new_item should be inserted next to it
    # and on the right at index of j+1

    # inserting
    A[j + 1] = new_item


def insertionSort(A):
    n = len(A)

    # we may start from 0
    # for i in range(0, n):
    #     insertItem(A, i)

    # we may start from 1, because it makes sense that there are at least 2 items.
    for i in range(1, n):
        insertItem(A, i)


# test
dataset = [5, 2, 1, 4, 3]
print("Original list")
print(dataset)
print()

print("After insertion sorting")
insertionSort(dataset)
print(dataset)