"""
insert an item to an ordered list (array)

new_item v.s. last item

repeat:
    if new_item <= current_item
        current_item does right shift by 1
    if new_item > current_item
        stop

get index of current_item
insert new_item at index of x+1
"""

orderedList = [1, 3, 5, 7, 9]
new_item = 4
last_item = 0
n = len(orderedList)
j = n - 1
current_item = last_item

orderedList.append(None)




while j > 0:
    if new_item <= orderedList[j]:
        orderedList[j+1] = orderedList[j]
        j = j - 1

    else:
        break

orderedList[j+1] = new_item
print(orderedList)
