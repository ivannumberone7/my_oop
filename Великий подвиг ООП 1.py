import random as rd

class Cell:
    def __init__(self, around_mines, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.init(N,M)

    def init(self, N, M):
        self.game_field = []
        for i in range(N):
            self.game_field.append(['*' for j in range(N)])
        new_g_f = self.paste_mine(self.gen_mine(N, M), self.game_field)
        self.game_field = new_g_f
        self.game_field = self.paste_cell(self.game_field)

    @classmethod
    def gen_mine(cls, N, M):
        indx_mine = []
        while M!=0:
            a = rd.randint(0, ((N*N) - 1))
            if a not in indx_mine:
                indx_mine.append(a)
                M = M-1
        return indx_mine

    @classmethod
    def paste_mine(cls, indx_mine, g_f):
        for ix_mine in indx_mine:
            a = ix_mine//len(g_f[0])
            b = ix_mine - (a*len(g_f[0]))
            g_f[a][b] = 'X'
        return g_f

    @staticmethod
    def paste_cell(field):
        for row in range(len(field)):
            for num in range(len(field[row])):
                numm = field[row][num]
                if numm == 'X':
                    c = Cell(0, True)
                    field[row][num] = c
        print(field)
        return field


    def show(self):
        for rows in self.game_field:
            pass
            #print(' '.join(rows))

g = GamePole(10,12)
g.show()