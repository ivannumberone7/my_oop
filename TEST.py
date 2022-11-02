# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     # здесь добавлять методы
#     def insert(self, data):
#         self.lst_data.append(dict(zip(self.FIELDS, data)))
#
#     def select(self, a, b):
#         return self.lst_data[a:b + 1]
#
#     def draw(self):
#         print(self.lst_data)
#
#
# a = ['1', '2', '3', '4']
#
# db = DataBase()
# for i in range(5):
#     db.insert(a)
# c = db.select(1, 2)
# db.draw()
# print(c)

# class Video:
#     def create(self,name):
#         self.name = name
#     def play(self):
#         print(f'Воспроизведение видео {self.name}')
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx-1].play()
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# YouTube.add_video(v1)
# v2.create('Python ООП')
# YouTube.add_video(v2)
# YouTube.play(1)
# YouTube.play(2)





# class Translator:
#
#     data = dict()
#
#     def add(self,eng,rus):
#         if eng in self.data.keys():
#             self.data[eng].append(rus)
#         else:
#             self.data[eng]=list()
#             self.data[eng].append(rus)
#     def remove(self,eng):
#         del self.data[eng]
#     def translate(self, eng):
#         res = self.data[eng]
#         return res
#
# tr = Translator()
# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
# tr.remove('car')
# r1 = tr.translate('go')
# print(*r1)
#
# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
# points = list()
# for i in range(1,201,2):
#     if i==3:
#         points.append(Point(i,i,'yellow'))
#     else:
#         points.append(Point(i,i))
# print(points[1].color)
# print(len(points))





# from random import choice, randint
#
# class Line:
#     def __init__(self,a,b,c,d):
#         self.sp = (a,b)
#         self.ep = (c,d)
#
# class Rect:
#     def __init__(self,a,b,c,d):
#         self.sp = (a,b)
#         self.ep = (c,d)
#
# class Ellipse:
#     def __init__(self,a,b,c,d):
#         self.sp = (a,b)
#         self.ep = (c,d)
# elements = []
# figures = [Line, Ellipse, Rect]
# for i in range(217):
#     elements.append(choice(figures)(randint(1,100),randint(1,100),randint(1,100),randint(1,100)))
# print(elements)
#
# for ele in elements:
#     if isinstance(ele, Line):
#         ele.ep = (0,0)
#         ele.sp = (0,0)


# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
#     def is_triangle(self):
#         if not isinstance(self.a, int) or not isinstance(self.b, int) or not isinstance(self.c, int):
#             return 1
#         if self.a <= 0 or self.b <= 0 or self.c <= 0:
#             return 1
#         if self.a + self.b > self.c or self.b + self.c > self.a or self.a + self.c > self.b:
#             return 3
#         else:
#             return 2
#
#
# a, b, c = map(int, input().split())  # эту строчку не менять
# # здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


# class Graph:
#
#     def __init__(self,data,is_show=True):
#         self.data = data
#         self.is_show = is_show
#         self.res = str(self.data)[1:len(str(self.data)) - 1].replace(',', '')
#
#     def set_data(self,data):
#         self.data+=data
#
#     def show_table(self):
#         if self.is_show:
#             print(self.res)
#         else:
#             print('Отображение данных закрыто')
#
#     def show_graph(self):
#         if self.is_show:
#             print(f'Графическое отображение данных: {self.res}')
#         else:
#             print('Отображение данных закрыто')
#
#     def show_bar(self):
#         if self.is_show:
#             print(f'Столбчатая диаграмма: {self.res}')
#         else:
#             print('Отображение данных закрыто')
#
#     def set_show(self, is_s):
#         self.is_show = is_s
#
# data_graph = list(map(int, input().split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()

# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
# class MotherBoard:
#     def __init__(self, name, cpu, mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mem_slots
#
#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                  f"Память: {'; '.join([f'{mem.name} - {mem.volume}' for mem in self.mem_slots])}"]
#
# mb = MotherBoard('Test',CPU('Test',4), [Memory('Test1',3), Memory('Test2',4)])
# print(mb.get_config())


# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cart:
#
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         print([f'{good.name}: {good.price}' for good in self.goods])
#
# cart = Cart()
# cart.add(TV('T1',5000))
# cart.add(TV('T2',66000))
# cart.add(Table('Stol',800))
# cart.add(Notebook('N1',39495))
# cart.add(Notebook('N2',7000))
# cart.add(Cup('Pivnaya',200))

# lst_in = ['1','2','3']
#
# class ListObject:
#     def __init__(self,data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1,len(lst_in)):
#     new_obj = ListObject(lst_in[i])
#     obj.next_obj = new_obj
#     obj = new_obj
