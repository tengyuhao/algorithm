"""
Python array
"""

import array as arr
# comparing arrays
mylist = [1, 2, 3, "Hello", 4.5]
print(type(mylist))

# create an array of integer items
myarray = arr.array('i', [1,2,3,4,5])
print(type(myarray))

# myarray = arr.array('i', [1, 2, 3, "Hello", 4.5])
# print(myarray)
# TypeError: an integer is required (got type str)

# create an array without intial items
myarray = arr.array('i')
print(myarray)



# create an array of character
mystr = arr.array('u', "hello world")
print(mystr)