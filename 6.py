# Инкапсуляция
class Point():

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls,a):
        return type(a) in (int,float)

    def set_coord(self,x,y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x=x
            self.__y=y
        else:
            raise ValueError('Введите числа')

    def get_coord(self):
        return self.__x, self.__y

pt = Point(1,2)
# у Питона не настоящая инкапсуляция
print(dir(pt)[1:3])
#print(pt._Point__x, pt._Point__y)

pt.set_coord(45.3,4)
print(pt.get_coord())

