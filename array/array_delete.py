"""
Python Array operations
insertion to a given index
"""

import array as arr

# create an array
myarray = arr.array('i', [1, 3, 5, 7, 8])
print("before insertion")
print("original array:",myarray)

# increase capacity by 1
SIZE_MYARR = len(myarray)
SIZE_NEWARR = SIZE_MYARR + 1
newarray = arr.array('i', range(SIZE_NEWARR))
for i in range(SIZE_MYARR):
    newarray[i] = myarray[i]
print("new array:", newarray)

# insert item=10 into array at index=3
print("\nitems to move")
ins_index = 3
for i in range(ins_index, SIZE_MYARR):
    print(f"myarray[{i}]={myarray[i]}")

print("\nmoving items")
# for i in range(SIZE_MYARR-1, ins_index-1, -1):
for i in range(SIZE_MYARR-1, ins_index, -1):
    newarray[i+1] = newarray[i]
    print(f"newarray[{i}] ->newarray[{i+1}]")

print("\nupdate item at ins_index")
new_item = 10
newarray[ins_index] = new_item
print(f"newarray[{ins_index}] <- {new_item}")

# traverse
print("\nafter insertion")
for i in range(len(newarray)):
    if i == 5:
        print(f"{newarray[i]}", end=", ")

    else:
        print(f"{newarray[i]}")
        break


