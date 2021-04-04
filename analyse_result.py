from tkinter import Tk, Toplevel, filedialog, Text, END
from tkinter.ttk import Frame, Button, Label, Entry, Scrollbar
from tkinter import BOTH, LEFT, Y, ALL, WORD, DISABLED, TOP, N


class AnalyseResultFrame(Frame):
    def __init__(self, parent: Tk or Toplevel, text: str = '', title: str= ''):
        Frame.__init__(self, parent)
        self.parent = parent
        self.text = text
        self.title = title

        self.title = Label(self, text=title)
        self.title.pack(side=TOP, anchor=N)

        self.textField = Text(self, height=30, width=50, wrap=WORD)
        self.scr = Scrollbar(self, command=self.textField.yview)

        self.textField.configure(yscrollcommand=self.scr.set)
        if self.text is not None:
            self.textField.insert(1., self.text)

        self.scr.pack(side="right", fill="y")
        self.textField.pack(side="left", fill="both", expand=True, pady=8)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


    def centerWindow(self):
        w = 570
        h = 600
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def set_text(self, text: str) -> None:
        self.text = text
        self.textField.delete('1.0', 'end')
        self.textField.insert(1.0, self.text)


def main():
    root = Tk()
    AnalyseResultFrame(root,
                       text="Тестовое окно\nSample text\nVery very very "
                            "very very very very very very very very very "
                            "very very very very very very very very very "
                            "very very very very very very very very very "
                            "very very very very very long text\n" * 50)
    root.mainloop()


if __name__ == "__main__":
    main()
