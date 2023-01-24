"""
operation
"""

mylist = [1, 2, 3, 4, 5]
myset = {11,21,31}
mydict = {1: 'a', 2:'b'}

# traversing
for i in mylist:
    print(i)

for i in myset:
    print(i)

for i in mydict:
    print(f"key:{i}, value:{mydict[i]}")

# searching
# by index
item2 = mylist[2]
pos = mylist.index(3)

# insertion
mylist.append("aaa")
mylist.extend(["aa","bb"])
mylist[2:2] = ["aaa","ddd"]

myset.add("aaa")

mydict[3] = "ccc"

# user-defined data type
print("=================")

class MyGarage:
    def __init__(self, cars=[], tools=[]):
        self.cars = cars
        self.tools = tools

    def add_car(self, mycar):
        """insertion"""
        self.cars.append(mycar)

    def add_tool(self, mytool):
        """insertion"""
        self.tools.append(mytool)

    def show_garage(self):
        """insertion"""
        print("show garage:")
        for car in self.cars:
            print(car)
        for tool in self.tools:
            print(tool)


garage = MyGarage()
# traverse
garage.show_garage()

# after insertion
garage.add_car("bmw")
garage.add_car("nissan")
garage.add_car("toyota")


garage.add_tool("drill")
garage.add_tool("screwer")
garage.add_tool("hammer")
# traverse
garage.show_garage()