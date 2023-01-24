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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person[name={self.name},age={self.age}]"


def bubblesort_by_field(objlist, fieldname, fieldname2):
    for j in range(len(objlist) - 1):
        swapped = False

        for i in range(len(objlist) - 1 - j):
            if getattr(objlist[i], fieldname) > getattr(objlist[i + 1], fieldname):
                # swap
                objlist[i], objlist[i + 1] = objlist[i + 1], objlist[i]
                swapped = True
            elif getattr(objlist[i], fieldname) == getattr(objlist[i + 1], fieldname):
                if getattr(objlist[i], fieldname2) > getattr(objlist[i + 1], fieldname2):
                    objlist[i], objlist[i + 1] = objlist[i + 1], objlist[i]
                    swapped = True

        # if no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return objlist


# test
# data
print("=== Original data set ===")
person_list = [Person(name, age) for (name, age) in (('Peter', 20), ("Bob", 22), ('Kevin', 21), ('Amy', 21), ('Amy', 19))]
for person in person_list:
    print(person)
print()

# sorting via bubble sort algo
print("=== bubble sort ===")
ordered_person_list = bubblesort_by_field(person_list, 'age', 'name')

# result
print("=== Result of sorting by age and name ===")
for person in ordered_person_list:
    print(person)

print("\n\n=========\n\n")

print("=== Original data set ===")
person_list = [Person(name, age) for (name, age) in (('Peter', 20), ("Bob", 22), ('Kevin', 21), ('Amy', 21), ('Amy', 19))]
for person in person_list:
    print(person)
print()

# sorting via bubble sort algo
print("=== bubble sort ===")
ordered_person_list = bubblesort_by_field(person_list, 'name', 'age')

# result
print("=== Result of sorting by name and age ===")
for person in ordered_person_list:
    print(person)
