from tkinter import *
from tkinter import messagebox


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemy = True
        self.hidden = True
        self.val = 'W'


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
        for i in range(10):
            for j in range(10):
                self.enemy[i].append(Square(i,j))
        self.player = [[]]

    def clicked(self, event):
        if self.game:
            if 350 <= event.x <= 550 and 50 <= event.y <= 250:
                x, y = self.enemyConvert(event.x, event.y)
                if self.enemy[x][y].hidden:
                    self.attack(x, y, 1)
        else:
            pass

    def attack(self, x, y, z):
        if z == 1:
            update

    def enemyConvert(self, x, y):
        if y > 10:
            x, y = x - 350, y - 350
            x, y = x // 20, y // 20
            return x, y
        else:
            return x * 20 + 350, y * 20 + 350

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

        self.canv.pack(padx=25, pady=25, anchor=E)

    def newGame(self):
        messagebox.showwarning(title='No Games Available', message='App still under development')

    def terminate(self):
        a = messagebox.askyesno(title='Exit?', message='Are you sure you\'d like to quit?')
        if a > 0:
            root.quit()

root = Tk()
root.title("Battleship!")
app = MainGame(root)

root.geometry("750x400+200+200")

root.mainloop()
