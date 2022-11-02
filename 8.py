# Паттерн МоноСостояние
# Все атрибуты экземпляров будут иметь 1 состояние
class ThreadData:
    __shared_dict = {
        'name':'thread_1',
         'data': {},
        'id':1
    }

    def __init__(self):
        self.__dict__ = self.__shared_dict

th1 = ThreadData()
th2 = ThreadData()
th2.id = 4
print(th1.__dict__)
print(th2.__dict__)