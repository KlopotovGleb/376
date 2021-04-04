import docx
from tkinter import filedialog
from tkinter import Tk, BOTH, Checkbutton, IntVar, BooleanVar
from tkinter.ttk import Frame, Button, Style
from typing import List, Any, Union


### Начало екбокса

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def centerWindow(self):
        w = 300
        h = 380
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initUI(self):
      #  self.master.title('Выберите параметры для анализа')
        self.pack(fill=BOTH, expand=True)
        #self.var = BooleanVar()
        self.parent.title('Выберите параметры для анализа')
        #self.style = Style()
        #self.style.theme_use("default")
        #names = ['Выравнивание абзаца', 'Отступ перед абзацем(см)', 'Отступ после абзаца(см)', 'Отступ слева(см)',
              #      'Отступ справа(см)', 'Отступ первой строки абзаца(см)', 'Не отрывать от следующего абзаца',
               #  'Не разрывать абзац', 'Абзац с новой страницы', 'Запрет висячих строк', 'Курсивный текст',
               #  'Полужирный текст', 'Подчёркнутый текст', 'Название шрифта', 'Размер шрифта(кегль)',
               #  'Цвет текста, RGB', 'Цвет заливки текста', 'Начать анализ']

        self.var1 = BooleanVar()
        cb1 = Checkbutton(self, text='Выравнивание абзаца', variable=self.var1)
        cb1.place(x=20, y=20)
        self.var2 = BooleanVar()
        cb1 = Checkbutton(self, text='Отступ перед абзацем(см)', variable=self.var2)
        cb1.place(x=20, y=40)
        self.var3 = BooleanVar()
        cb1 = Checkbutton(self, text='Отступ после абзаца(см)', variable=self.var3)
        cb1.place(x=20, y=60)
        self.var4 = BooleanVar()
        cb1 = Checkbutton(self, text='Отступ слева(см)', variable=self.var4)
        cb1.place(x=20, y=80)
        self.var5 = BooleanVar()
        cb1 = Checkbutton(self, text='Отступ справа(см)', variable=self.var5)
        cb1.place(x=20, y=100)
        self.var6 = BooleanVar()
        cb1 = Checkbutton(self, text='Отступ первой строки абзаца(см)', variable=self.var6)
        cb1.place(x=20, y=120)
        self.var7 = BooleanVar()
        cb1 = Checkbutton(self, text='Не отрывать от следующего абзаца', variable=self.var7)
        cb1.place(x=20, y=140)
        self.var8 = BooleanVar()
        cb1 = Checkbutton(self, text='Не разрывать абзац', variable=self.var8)
        cb1.place(x=20, y=160)
        self.var9 = BooleanVar()
        cb1 = Checkbutton(self, text='Абзац с новой страницы', variable=self.var9)
        cb1.place(x=20, y=180)
        self.var10 = BooleanVar()
        cb1 = Checkbutton(self, text='Запрет висячих строк', variable=self.var10)
        cb1.place(x=20, y=200)
        self.var11 = BooleanVar()
        cb1 = Checkbutton(self, text='Курсивный текст', variable=self.var11)
        cb1.place(x=20, y=220)
        self.var12 = BooleanVar()
        cb1 = Checkbutton(self, text='Полужирный текст', variable=self.var12)
        cb1.place(x=20, y=240)
        self.var13 = BooleanVar()
        cb1 = Checkbutton(self, text='Подчёркнутый текст', variable=self.var13)
        cb1.place(x=20, y=260)
        self.var14 = BooleanVar()
        cb1 = Checkbutton(self, text='Название шрифта', variable=self.var14)
        cb1.place(x=20, y=280)
        self.var15 = BooleanVar()
        cb1 = Checkbutton(self, text='Размер шрифта(кегль)', variable=self.var15)
        cb1.place(x=20, y=300)
        self.var16 = BooleanVar()
        cb1 = Checkbutton(self, text='Цвет текста, RGB', variable=self.var16)
        cb1.place(x=20, y=320)
        self.var17 = BooleanVar()
        cb1 = Checkbutton(self, text='Цвет заливки текста', variable=self.var17)
        cb1.place(x=20, y=340)
        self.var18 = BooleanVar()


        #cb[i] = Checkbutton(self, text=names[i], variable=self.var, command=self.onClick)
        #cb1.place(x=50, y=50)

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text='Начать анализ', command=self.quit)
        quitButton.place(x=200, y=200)

        print(self.var1.get())
        print(self.var2.get())
        print(self.var3.get())
        print(self.var4.get())
        print(self.var5.get())
        print(self.var6.get())
        print(self.var7.get())
        print(self.var8.get())
        print(self.var9.get())
        print(self.var10.get())
        print(self.var11.get())
        print(self.var12.get())
        print(self.var13.get())
        print(self.var14.get())
        print(self.var15.get())
        print(self.var16.get())
        print(self.var17.get())



def main():
    root = Tk()
    root.geometry()
    Example(root)
    root.mainloop()

###Конец чекбокса
if __name__ == '__main__':
    main()

