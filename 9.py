class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    oldd = property(get_age, set_age)

p = Person('Ivan',23)
p.__dict__['oldd'] = 'slova'
print(p.__dict__)
#p.oldd = 44
print(p.oldd)


class Person1:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age



p1 = Person('Ivan',23)
p1.age = 44
print(p1.age)