import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        

    
    

x1 = int(input("input x1\n"))
y1 = int(input("input y1\n"))

x2 = int(input("input x2\n"))
y2 = int(input("input y2\n"))

a = Point(x1, y1)
b = Point(x2, y2)

print (f'{a.distance(b):.2f}')


