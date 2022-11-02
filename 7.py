class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD and self.MIN_COORD <= y <= self.MAX_COORD:
            self.x = x
            self.y = y

    def set_min_coord(self, min):
        # создасться новая переменная в области экземпляра, атрибут класса
        # не поменяется
        self.MAX_COORD = min

    def __getattribute__(self, item):
        # Переопределение get_attr
        if item=='x':
            raise ValueError('Доступ закрыт')
        else:
            return object.__getattribute__(self,item)

pt1 = Point(12,33)
pt2 = Point(1,2)
#print(pt1.__dict__)
print(pt1.y)
print(Point.__dict__)


