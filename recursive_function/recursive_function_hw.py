"""
Write a program to get the nth number of fibonacci sequences.
"""


def fibonacci(n):
    if n <= 1:
        return n

    # elif n <=0:
    #     return "Number didn't support"

    else:
        ans = fibonacci(n-1) + fibonacci(n-2)
        return ans


# main program
terms = 20
for i in range(terms):
    print(fibonacci(i))

