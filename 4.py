# Магический метод new
class Point():
    def __new__(cls, *args, **kwargs): #args и kwargs нужны для передачи аргументов
        # запускает создание экземпляра класса
        # возвращает адрес экземпляра класса
        print(args)
        print(f'__new__ for {cls}')
        return super().__new__(cls) #ссылка на базовый класс (без этого не будет
    # работать инит) Наследование от базового класса object

    def __init__(self,x=0,y=0):
        print(f'__init__ for {self}')
        self.x = x
        self.y = y

pt = Point(1,2)
print(pt)