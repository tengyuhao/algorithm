"""
Bubble Sort
"""


def bubble_sort(a):
    n = len(a)

    def swap(a, x, y):
        x, y = y, x

    for j in range(n - 1):
        for i in range(n - 1 - j):
            if a[i+1] < a[i]:
                swap(a, a[i], a[i+1])
                swapped = True

        if not swapped:
            break

    return a


# main program
L = [5, 1, 3, 4, 2]
print(bubble_sort(L))

