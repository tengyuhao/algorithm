"""
Insert an item of number to an array
"""

import array as arr

# create an array of integer items
myarray = arr.array('i', [1,3,5,7,8])
print(type(myarray))

myarray.insert(3, 10)
print(myarray)

"""
Rewrite from C
"""


def main():
    LA = arr.array('i', [1, 3, 5, 7, 8])

    print("The original array elements are:\n")
    for i in range(len(LA)):
        print(f"LA[{i}]={LA[i]}")

    j = len(LA)

    item = 10
    while(j >= item):
        LA[j+1] = LA[j]
        j = j - 1

    print("The array elements after insertion :\n")
    for i in range(len(LA)):
        print(f"LA[{i}]={LA[i]}")

    print(LA)


if __name__ == "__main__":
    main()