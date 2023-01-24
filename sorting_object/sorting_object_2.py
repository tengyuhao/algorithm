
import operator

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
person_list.append(Person("Amy", 21, 87))
person_list.append(Person("Cindy", 18, 90))
person_list.append(Person("David", 20, 87))

comparator = operator.attrgetter("name", "age", "score")
person_list.sort(key=comparator)
for p in person_list:
    print(p)