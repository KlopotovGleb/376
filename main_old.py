from tkinter import Tk, BOTH, BooleanVar, Checkbutton, Toplevel,\
        LabelFrame, LEFT, RIGHT, Y, TOP, W, N, E
from tkinter.ttk import Frame, Button
from params import PARAMS
from input_param_щдвs import ParamsInputFrame
import tkinter.messagebox as mb


class ParamSelectionFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.user_selected = {param_id: BooleanVar() for param_id in PARAMS.keys()}

        self.pack(fill=BOTH, expand=1)
        self.initUI()

    def centerWindow(self):
        w = 360
        h = 380
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initUI(self):
        self.centerWindow()
        self.pack(fill=BOTH, expand=True)
        self.parent.title('Выберите параметры для анализа')

        container1 = Frame(self)

        group = LabelFrame(container1, text='Шрифт')
        group.pack(side=TOP, fill=BOTH, expand=True)

        group2 = LabelFrame(container1, text='Абзац')
        group2.pack(side=TOP, fill=BOTH, expand=True)

        i = 0
        for param_id, param in PARAMS.items():
            if i < 4:
                but = Checkbutton(group,
                                  text=param.name,
                                  variable=self.user_selected[param_id])
                but.grid(row=i, sticky=W, padx=(5, 25))
            else:
                but = Checkbutton(group2,
                                  text=param.name,
                                  variable=self.user_selected[param_id])
                but.grid(row=i, sticky=W, padx=(5, 25))
            i += 1

        container1.pack(side=LEFT, fill=BOTH)

        quitButton = Button(self, text="Продолжить", command=self.goAnalyse)
        quitButton.pack(padx=15, side=LEFT)

    def goAnalyse(self):
        needed_params = [
            param_id for param_id in PARAMS.keys() if self.user_selected[param_id].get()
        ]
        print(needed_params)
        window = Toplevel(self)
        ParamsInputFrame(window, needed_params)


def main():
    root = Tk()
    ParamSelectionFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()

