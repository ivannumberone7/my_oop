# Методы классов и self
class Point():
    color = 'red'
    circle = 1


    def set_coords(self,x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        print(f'coords: {self.x} {self.y}')
a = Point()
a.set_coords(4,5)
a.get_coords()