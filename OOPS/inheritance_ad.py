class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Humans(Animals):
    def __init__(self, name, age, detail):
        super().__init__(name, age)
        self.detail = detail

obj = Humans("random", 18, 222)

print(f"{obj.name} {obj.age}")

class Ani:
    def __init__(self, abc):
        self.abc = abc

class Hum:
    def __init__(self, id):
        self.id = id

class Robots(Hum, Ani):
    def __init__(self, abc, id):
        Hum.__init__(self,id)
        Ani.__init__(self, abc)

robo = Robots(12, 18)
print(f"{robo.abc} and {robo.id}")

# non working code
# def __add__(self, other):
#     return self + other

# __add__(1, 2)
