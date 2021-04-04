from tkinter import*
class Test:
    all_answer = []


    def __init__(self, master):
        self.master = master
        frame = Frame(master, height=400, width=380)
        self.master.title('Введите параметры для анализа')
        frame.pack_propagate(0)
        frame.pack()
        self.addButton = Button(frame, text="Начать анализ", command=self.new_test)
        self.addButton.place(x=247, y=360)

        self.lbl1 = Label(frame, text="Выравнивание абзаца: ")
        self.lbl1.place(x=10, y=10)
        self.number1 = Entry(frame)
        self.number1.place(x=230, y=10)

        self.lbl2 = Label(frame, text="Отступ перед абзацем: ")
        self.lbl2.place(x=10, y=30)
        self.number2 = Entry(frame)
        self.number2.place(x=230, y=30)

        self.lbl3 = Label(frame, text="Отступ после абзаца: ")
        self.lbl3.place(x=10, y=50)
        self.number3 = Entry(frame)
        self.number3.place(x=230, y=50)

        self.lbl4 = Label(frame, text="Отступ слева: ")
        self.lbl4.place(x=10, y=70)
        self.number4 = Entry(frame)
        self.number4.place(x=230, y=70)

        self.lbl5 = Label(frame, text="Отступ справа: ")
        self.lbl5.place(x=10, y=90)
        self.number5 = Entry(frame)
        self.number5.place(x=230, y=90)

        self.lbl6 = Label(frame, text="Отступ первой строки абзаца: ")
        self.lbl6.place(x=10, y=110)
        self.number6 = Entry(frame)
        self.number6.place(x=230, y=110)

        self.lbl7 = Label(frame, text="Не отрывать от следующего абзаца: ")
        self.lbl7.place(x=10, y=130)
        self.number7 = Entry(frame)
        self.number7.place(x=230, y=130)

        self.lbl8 = Label(frame, text="Не разрывать абзац: ")
        self.lbl8.place(x=10, y=150)
        self.number8 = Entry(frame)
        self.number8.place(x=230, y=150)

        self.lbl9 = Label(frame, text="Абзац с новой страницы: ")
        self.lbl9.place(x=10, y=170)
        self.number9 = Entry(frame)
        self.number9.place(x=230, y=170)

        self.lbl10 = Label(frame, text="Запрет висячих строк: ")
        self.lbl10.place(x=10, y=190)
        self.number10 = Entry(frame)
        self.number10.place(x=230, y=190)

        self.lbl11 = Label(frame, text="Курсивный текст: ")
        self.lbl11.place(x=10, y=210)
        self.number11 = Entry(frame)
        self.number11.place(x=230, y=210)

        self.lbl12 = Label(frame, text="Полужирный текст: ")
        self.lbl12.place(x=10, y=230)
        self.number12 = Entry(frame)
        self.number12.place(x=230, y=230)

        self.lbl13 = Label(frame, text="Подчёркнутый текст: ")
        self.lbl13.place(x=10, y=250)
        self.number13 = Entry(frame)
        self.number13.place(x=230, y=250)

        self.lbl14 = Label(frame, text="Название шрифта: ")
        self.lbl14.place(x=10, y=270)
        self.number14 = Entry(frame)
        self.number14.place(x=230, y=270)

        self.lbl15 = Label(frame, text="Размер шрифта(кегль): ")
        self.lbl15.place(x=10, y=290)
        self.number15 = Entry(frame)
        self.number15.place(x=230, y=290)

        self.lbl16 = Label(frame, text="Цвет текста, RGB: ")
        self.lbl16.place(x=10, y=310)
        self.number16 = Entry(frame)
        self.number16.place(x=230, y=310)

        self.lbl17 = Label(frame, text="Цвет заливки текста: ")
        self.lbl17.place(x=10, y=330)
        self.number17 = Entry(frame)
        self.number17.place(x=230, y=330)

    def new_test(self):
        root = Tk()
        s = int(self.number.get())
        s1 = int(self.number_of_answer1.get())

        frame = Frame(root, height=1000, width=500)
        frame.pack_propagate(0)
        frame.pack()
        states = []
        for i in range(s):
            for z in range(s1):
                var = IntVar()
                chk = Checkbutton(frame, text=str(z), variable=var)
                chk.grid(row=i, column=z)
                states.append(var)
        addTest = Button(frame, text="PRINT")
        addTest.grid(row=s+1,column=0)
        addTest.bind("<Button-1>", lambda event: self.kkk(states))

    def kkk(self, all):
        a = [int(item.get()) for index, item in enumerate(all)]
        print(a)


root = Tk()
b = Test(root)
root.mainloop()