"""
Module: sorting_objects_1.py

sorting objects in Python
not using APIs
with method of Bubble sort

sorting by double properties

getattr()
getattr(object,name) -> object.name
"""


class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"Person[name={self.name},age={self.age}, score={self.score}]"


def bubblesort_by_field(objlist, properties):
    for j in range(len(objlist) - 1):
        swapped = False

        index = 0

        for i in range(len(objlist) - 1 - j):

            def mysort(index):
                nonlocal swapped

                if index == len(properties):
                    return

                if getattr(objlist[i], properties[index]) > getattr(objlist[i + 1], properties[index]):
                    # swap
                    objlist[i], objlist[i + 1] = objlist[i + 1], objlist[i]
                    swapped = True
                elif getattr(objlist[i], properties[index]) == getattr(objlist[i + 1], properties[index]):
                    index += 1
                    mysort(index)

            mysort(index)

        # if no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return objlist


# test
# data
print("=== Original data set ===")
person_list = [Person(name, age, score) for (name, age, score) in
               (('Peter', 20, 83), ("Bob", 22, 83), ('Kevin', 21, 67), ('Amy', 21, 90), ('Amy', 19, 90))]
for person in person_list:
    print(person)
print()

# sorting via bubble sort algo
print("=== bubble sort ===")
propeties = ['score', 'name', 'age']
# propeties = ['score']
ordered_person_list = bubblesort_by_field(person_list, propeties)

# result
print("=== Result of sorting by score, name, and age ===")
for person in ordered_person_list:
    print(person)
