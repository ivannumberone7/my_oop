# статические методы и методы класса
class Vector:

    min_coord = 0
    max_coord = 100

    # метод класса работает только с атрибутами класса, но не экземпляров
    # cls = сам класс
    @classmethod
    def validate(cls, arg):
        return cls.min_coord<=arg<=cls.max_coord

    def __init__(self,x,y):
        self.x = self.y = 0
        # if Vector.validate(x): - тоже можно, но лучше self
        if self.validate(x):
            self.x = x
        if self.validate(y):
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    # не работает ни с параметрами класса, ни с па-ми экземпляра
    # независимая от других параметров класса, экзпемпляров
    def norm2(x,y):
        return x**2 + y**2

v = Vector(-9,3)
res = v.get_coord()
print(res)
res1 = Vector.validate(4)
print(res1)
print(Vector.norm2(44,55))