# Классы и атрибуты

class Point():
    color = 'red'
    circle = 1

print(Point.__dict__)
setattr(Point, 'x', 1)
print(Point.__dict__)
x = getattr(Point, 'x')
print(x)
a = Point()
print(a.__dict__)
print(hasattr(Point, 'color'))
print(hasattr(a, 'color'))
a.color = 'blue'
a.y = 5
print(a.__dict__)
delattr(Point, 'circle')
print(a.__dict__)
#print(a.circle) # error




print('Хуй соси')