"""
3. Write programs and understand the procedure to apply bubble sort algorithms to a real problem of sorting
business objects by its property(s). (10')
filename:  stem1401_final_p3.py
please write 3.1, 3.2, 3.3 into the above source code file.
3.1 Create a user-defined class (10')
class name:	Person
properties:	name, age
constraints:	a constructor and a method of __str__ are required.
3.2 Write a program to sort 5 Person objects in ascending order by its property of name. (10')
Person objects:
Person ('Peter', 20),
Person ("Bob", 22),
Person ('Kevin', 21),
Person ('Amy', 21),
Person ('Amy', 19)
3.3 Write a program to sort 5 Person objects in ascending order by its property of age. (10')
Person objects:
the same as previous problem 3.2
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"[{self.name}, {self.age}]"


def sort_name(a):
    n = len(a)

    def swap(a, x, y):
        a[i], a[i + 1] = a[i + 1], a[i]

    for j in range(n - 1):
        for i in range(n - 1):
            if a[i + 1].name < a[i].name:
                swap(a, a[i], a[i + 1])

    return a


def sort_age(a):
    n = len(a)

    def swap(a, x, y):
        a[i], a[i + 1] = a[i + 1], a[i]

    for j in range(n - 1):
        for i in range(n - 1):
            if a[i + 1].age < a[i].age:
                swap(a, a[i], a[i + 1])

    return a


# info
p1 = Person('Peter', 20)
p2 = Person("Bob", 22)
p3 = Person('Kevin', 21)
p4 = Person('Amy', 21)
p5 = Person('Amy', 19)

# main program
person_list = [p1, p2, p3, p4, p5]
# print(person_list)
print("Sort by name:")
sort_name(person_list)
for i in person_list:
    print(i)
print()
print("Sort by age:")
sort_age(person_list)
for i in person_list:
    print(i)


