
class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"[{self.name}, {self.age}]"


person_list = []
person_list.append(Person("Emma", 19, 83))
person_list.append(Person("Amy", 20, 83))
person_list.append(Person("Bobby", 21, 87))
person_list.append(Person("Cindy", 18, 90))
person_list.append(Person("David", 20, 87))

# sort by name
print("=== sort by name ===")
person_list.sort(key=lambda p:p.name)
for p in person_list:
    print(p)

print("=== sort by age ===")
person_list.sort(key=lambda p: p.age)
for p in person_list:
    print(p)

print("=== sort by list ===")
person_list.sort(key=lambda p: p.score)
for p in person_list:
    print(p)
