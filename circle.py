class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 *(self.radius ** 2)
    def perimeter(self):
    return 3.14159 *(self.radius ** 2)

    


re = int(input("Enter the radius: "))
obj = circle(re)
print(obj.radius)
print(obj.area())

print(obj.perimeter())
