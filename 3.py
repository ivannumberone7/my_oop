# Магические методы инциализатор и финализатор
class Point():
    color = 'red'
    circle = 1

    def __init__(self, a=0, b=0):
        print('Создаётся экземпляр класса')
        self.x = a
        self.y = b

    def __del__(self):
        print('Удаление экземпляра: '+str(self))

    def set_coords(self,x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        print(f'coords: {self.x} {self.y}')

a = Point()
print(a.__dict__)
a.set_coords(4,5)
print(a.__dict__)
a = 5 # сборщик мусора не удаляет объект, пока существует ссылка на него
print('The end')