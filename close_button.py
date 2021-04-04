from tkinter import Tk, BOTH, BooleanVar, Checkbutton
from tkinter.ttk import Frame, Button, Style
from typing import List, Any, Union


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def centerWindow(self):
        w = 400
        h = 380
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initUI(self):
        #self.master.title('Выберите параметры для анализа')
        self.pack(fill=BOTH, expand=True)
        #self.var = BooleanVar()
        self.parent.title('Выберите параметры для анализа')
        #self.style = Style()
        #self.style.theme_use("default")
        #variables = [BooleanVar()] * 17
        names = ['Выравнивание абзаца', 'Отступ перед абзацем(см)', 'Отступ после абзаца(см)', 'Отступ слева(см)',
                    'Отступ справа(см)', 'Отступ первой строки абзаца(см)', 'Не отрывать от следующего абзаца',
                 'Не разрывать абзац', 'Абзац с новой страницы', 'Запрет висячих строк', 'Курсивный текст',
                 'Полужирный текст', 'Подчёркнутый текст', 'Название шрифта', 'Размер шрифта(кегль)', 
                 'Цвет текста, RGB', 'Цвет заливки текста', 'Продолжить']
        cb = []
        for i in range(17):
            self.var = BooleanVar()
            cb.append(Checkbutton(self, text=names[i], variable=self.var))
            cb[i].place(x=20, y=20*(i+1))
        #cb[i] = Checkbutton(self, text=names[i], variable=self.var, command=self.onClick)
        #cb1.place(x=50, y=50)

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text=names[17], command=self.quit)
        quitButton.place(x=280, y=170)


    #def onClick(self):
        #if self.var.get():


def main():
    root = Tk()
    root.geometry()
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()