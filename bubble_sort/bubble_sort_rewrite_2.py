"""
Bubble Sort
"""


def bubble_sort(a):
    n = len(a)

    def swap(a, x, y):
        a[i], a[i + 1] = a[i + 1], a[i]

    for j in range(n - 1):
        for i in range(n - 1):
            if a[i+1] < a[i]:
                swap(a, a[i], a[i+1])

    return a


# main program
L = [5, 1, 3, 4, 2]
print(bubble_sort(L))

