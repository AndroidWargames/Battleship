from tkinter import *
from tkinter import messagebox
from random import randint


class Square:
    def __init__(self, x, y, enemy):
        self.x = x
        self.y = y
        self.enemy = enemy
        self.hidden = True
        self.val = 'w'


class MainGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createMenu()

        self.canv = Canvas(root, height=350, width=600, bg='gray')
        self.canv.bind('<Button-1>', self.clicked)

        self.createBoard()

        self.game = True
        #self.create_difficulty()
        self.focus_set()

        self.enemy = [[] for x in range(10)]
        self.player = [[] for x in range(10)]
        for i in range(10):
            for j in range(10):
                self.enemy[i].append(Square(i, j, True))
                self.player[i].append(Square(i, j, False))
        self.seek = True
        self.dir = [0, 1]

    def clicked(self, event):
        # if game is afoot
        if self.game:
            # if clicking enemy board, get small coordinates
            if 350 <= event.x <= 550 and 50 <= event.y <= 250:
                x, y = self.enemyConvert(event.x, event.y)
                # if square was unclicked, reveal square, do stuff, pass turn
                if self.enemy[x][y].hidden:
                    self.attack(x, y, 1)
                    self.enemyFire()

        else:
            pass

    def attack(self, x, y, z):
        # test if enemy or not, return square object, get big coordinates
        if z == 1:
            a = self.enemy[x][y]
            x1, y1 = self.enemyConvert(x, y)
            # enemy hits need to add color for ship
            if a.val != 'w':
                self.canv.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='gray')
        else:
            a = self.player[x][y]
            x1, y1 = self.playerConvert(x,y)

        # if it's a miss, print water
        if a.val == 'w':
            self.canv.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='blue')
        # otherwise, a red X for a hit
        else:
            self.canv.create_line(x1, y1, x1 + 20, y1 + 20, fill='red')
            self.canv.create_line(x1+20, y1, x1, y1 + 20, fill='red')
        # reload board
        a.hidden = False
        self.pact()

    def enemyFire(self):
        x = randint(0,9)
        y = randint(0,9)
        while not self.player[x][y].hidden:
            x = randint(0,9)
            y = randint(0,9)
        self.attack(x, y, 0)

    def enemyConvert(self, x, y):
        if y > 10:
            x, y = x - 350, y - 50
            x, y = x // 20, y // 20
            return x, y
        else:
            return x * 20 + 350, y * 20 + 50

    def playerConvert(self, x, y):
        if y > 10:
            x, y = x - 50, y - 50
            x, y = x // 20, y // 20
            return x, y
        else:
            return x * 20 + 50, y * 20 + 50

    def createMenu(self):
        menubar = Menu(root)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New", command=self.newGame)
        fileMenu.add_command(label="Quit", command=self.terminate)
        menubar.add_cascade(label='File', menu=fileMenu)
        root.config(menu=menubar)

    def createBoard(self):
        # draw water
        self.canv.create_rectangle(50, 50, 250, 250, fill='light blue')
        self.canv.create_rectangle(350, 50, 550, 250, fill='light blue')

        # draw borders
        for i in range(11):
            x = 50 + 20 * i

            self.canv.create_line(x, 50, x, 250)
            self.canv.create_line(50, x, 250, x)

            self.canv.create_line(x + 300, 50, x + 300, 250)
            self.canv.create_line(350, x, 550, x)
            self.pact()

    def pact(self):
        self.canv.pack(padx=25, pady=25, anchor=E)

    def newGame(self):
        self.enemy = [[] for x in range(10)]
        self.player = [[] for x in range(10)]
        for i in range(10):
            for j in range(10):
                self.enemy[i].append(Square(i, j, True))
                self.player[i].append(Square(i, j, False))
        self.createBoard()

    def terminate(self):
        a = messagebox.askyesno(title='Exit?', message='Are you sure you\'d like to quit?')
        if a > 0:
            root.quit()

root = Tk()
root.title("Battleship!")
app = MainGame(root)

root.geometry("750x400+200+200")

root.mainloop()
