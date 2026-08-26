class Test:
    a = 12

    def func():
        print("Hello World!")

print(Test.a)
Test.func()

class Bags:

    name = "random"

    def __init__(self, material, zip, pockets):
        self.material = material
        self.zip = zip
        self.pockets = pockets

    def random(self):
        print(f"my name is {self.material}")
        print(f"my name is {Bags.name}")

    @classmethod
    def another(cls):
        print(f"my name is {cls.name}")

    @staticmethod
    def smthng():
        print("smthng")

reebok = Bags("polyster", 3, 3)
campus = Bags("cotton", 2, 4)

print(f"{reebok.material} {campus.zip}")
Bags.smthng()
Bags.another()
reebok.random()