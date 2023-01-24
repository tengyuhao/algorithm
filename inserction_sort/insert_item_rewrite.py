"""
Insertion Sort
"""


def insertion(ordered_list, new_item):
    n = len(ordered_list)
    j = n - 1
    ordered_list.append(None)

    while j > 0:
        if new_item <= ordered_list[j]:
            ordered_list[j+1] = ordered_list[j]
            j = j - 1

        else:
            break

    ordered_list[j+1] = new_item
    return ordered_list


# main program
l = [1, 3, 5, 7, 9]
print(insertion(l, 4))




