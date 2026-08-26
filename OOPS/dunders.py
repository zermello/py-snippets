class random:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

num1 = random(2)
num2 = random(3)

huh = random.__add__(num1, num2)
print(huh)