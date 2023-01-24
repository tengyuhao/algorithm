"""
Bubble Sort
"""

a = [5, 1, 3, 4, 2]

def bubble_sort(a):
    N = len(a)

    def swap(a, x, y):
        a[i], a[i + 1] = a[i + 1], a[i]

    for j in range(N - 1):
        for i in range(N-1):
            if a[i+1] < a[i]:
                swap(a, a[i], a[i+1])

    return print(a)

bubble_sort(a)
