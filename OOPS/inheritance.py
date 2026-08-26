# Benefits of using inheritance is :
# • Code reusability
# • Organized structure
# • Easy to maintain and extend

class Animals():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Humans(Animals):
    pass

objj = Animals("heaven", 7)
obj = Humans("shon", 7)

print(f"{objj.name}")
print(f"{obj.name} and age is {obj.age}")