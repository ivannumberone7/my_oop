from string import ascii_letters

class Person:

    RUS_LET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    RUS_LET_UP = RUS_LET.upper()

    def __init__(self, fio, old, ps, wght):
        self.verify_fio(fio)

        self.__fio = fio
        self.old = old
        self.ps = ps
        self.weight = wght

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('Неверный тип данных. ФИО должна быть строкой.')
        else:
            fio = fio.split()
        if len(fio) !=3 :
            raise TypeError('Неверно ввели данные. Введите ФИО через пробел.')
        letters = cls.RUS_LET+cls.RUS_LET_UP+ascii_letters+'-'
        for word in fio:
            for let in word:
                if let not in letters:
                    raise TypeError('Присутствуют недопустимые символы. Пожалуйста, повторите ввод.')

    @classmethod
    def verify_old(cls, old):
        if type(old)!=int:
            raise TypeError('Возраст должен быть целым числом!')
        if 14<=old<=120:
            pass
        else:
            raise TypeError('Некорректное значение возраста')

    @classmethod
    def verify_passport(cls, ps):
        if type(ps) != str:
            raise TypeError('Неверный тип данных. Номер и серия пасспорта-строка.')
        else:
            ps = ps.split()
        if len(ps) != 2:
            raise TypeError('Неверно ввели данные. Введите номер и серию паспорта через пробел.')
        if len(ps[0]) != 4:
            raise TypeError('Неверно ввели данные. Серия паспорта должна состоять из 4 цифр.')
        if len(ps[1]) != 8:
            raise TypeError('Неверно ввели данные. Номер паспорта должен состоять из 8 цифр.')
        nums = '0123456789'
        for obj in ps:
            for num in obj:
                if num not in nums:
                    raise TypeError('Серия и номер паспорта должны состоять только из цифр!')

    @classmethod
    def verify_weight(cls, wght):
        try:
            wght = float(wght)
        except:
            raise TypeError('Вес должен быть числом!')
        if wght<20:
            raise TypeError('Некорректное значение веса')

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old=old

    @property
    def ps(self):
        return self.__passport

    @ps.setter
    def ps(self, ps):
        self.verify_passport(ps)
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

p = Person('Моисеенко Иван Юрьевич', 24, '1131 22222222', 130)
print(p.__dict__)
p.old = 32
print(p.__dict__)