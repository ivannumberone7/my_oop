# Пример паттерна SingleTon
# В момент выполнения программы должен существовать только 1 экземпляр этого класса

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
    # проверка на существование только одного объекта
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user,psw,port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instance = None

    def connect(self):
        print(f'Соединение: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Разъединение от БД')

    def read(self):
        return 'данные из БД'

    def write(self, data):
        print(f'Запись в БД:  {data}')

db = DataBase('root','123','80')
db2 = DataBase('root2','423','90')
print(id(db)==id(db2)) #создасться ссылка только на 1 объект
# но это неполный синглтон
db.connect()
db2.connect()
