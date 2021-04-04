from tkinter import Tk, Toplevel, filedialog, StringVar, LabelFrame
from tkinter.ttk import Frame, Button, Label, Entry, Radiobutton, Combobox
from tkinter import BOTH, TOP, W, LEFT

from typing import List

from analyse_result import AnalyseResultFrame
from params import Parameter, PARAMS

import docx


class ParamsInputFrame(Frame):
    def __init__(self, parent: Tk or Toplevel, param_ids: List[int]):
        Frame.__init__(self, parent)
        self.parent = parent
        self.param_ids = param_ids
        self.paragraph_params = [param_id for param_id in param_ids if not PARAMS[param_id].is_run]
        self.run_params = [param_id for param_id in param_ids if PARAMS[param_id].is_run]

        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.parent.title('Введите параметры для анализа')

        self.user_input = {param_id: StringVar() for param_id in self.param_ids}

        container1 = Frame(self)

        group = LabelFrame(container1, text='Шрифт')
        group.pack(side=TOP, fill=BOTH, expand=True)

        group2 = LabelFrame(container1, text='Абзац')
        group2.pack(side=TOP, fill=BOTH, expand=True)

        indent = 0
        i = 0
        for param_id in self.param_ids:
            param = PARAMS[param_id]
            if i < 4:
                current_group = group
            else:
                current_group = group2
            lbl = Label(current_group, text=param.name)
            lbl.grid(row=i, sticky=W, padx=(5, 25))
            if param.is_boolean:
                radio_btn = Radiobutton(current_group, variable=self.user_input[param_id], value="Нет")
                radio_btn.grid(row=i, column=1, sticky=W, padx=(5, 25))
            i += 1
        #
        #         lbl_yes = Label(self, text="Нет")
        #         lbl_yes.grid(row=i, sticky=W, padx=(5, 25))
        #
        #         # radio_btn = Radiobutton(self, variable=self.user_input[param_id], value="Да")
        #         # radio_btn.place(x=scnd_row_x + 50, y=10 + indent)
        #         #
        #         # lbl_yes = Label(self, text="Да")
        #         #
        #         # lbl_yes.place(x=scnd_row_x + 70, y=10 + indent)
        #         # self.user_input[param_id].set("Нет")
        #
        #     else:
        #         text_field = Combobox(self, textvariable=self.user_input[param_id])
        #         text_field['values'] = param.default_vals
        #         text_field.current(param.start_val)
        #         text_field.grid(row=i, sticky=W, padx=(5, 25))
        #
        #     indent += 23

        container1.pack(side=LEFT, fill=BOTH)

        self.addButton = Button(self, text="Начать анализ", command=self.new_test)
        self.addButton.pack(padx=15, side=LEFT)

    def centerWindow(self):
        w = 440
        h = 440
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def new_test(self):
        files = filedialog.askopenfilenames()
        if not files:
            return

        result_string = ""
        for path in files:
            doc = docx.Document(path)
            print("Working with file", path)
            result_string += f"Файл {path}\n"
            for section in doc.sections:
                print(section)
            for paragraph_ind, paragraph in enumerate(doc.paragraphs):
                formatting = paragraph.paragraph_format
                par_string = ""
                for param_id in self.paragraph_params:
                    param = PARAMS[param_id]
                    print(f"Analyzing param {param.name}")
                    user_input_val = self.user_input[param_id].get()
                    in_doc_val = str(param.getter(formatting))
                    if user_input_val.strip() != in_doc_val.strip():
                        par_string += f"{param.name}: {user_input_val} " \
                                      f"--- {in_doc_val}\n"

                if not self.run_params:
                    continue

                for run_id, run in enumerate(paragraph.runs):
                    run_string = ""
                    for param_id in self.run_params:
                        param = PARAMS[param_id]
                        user_input_val = self.user_input[param_id].get()
                        in_doc_val = str(param.getter(run))
                        if user_input_val.strip() != in_doc_val.strip():
                            run_string += f"{param.name}: {user_input_val} " \
                                          f"--- {in_doc_val}\n"
                        if run_string:
                            par_string += f"Run {run_id + 1}\n{run_string}"

                if par_string:
                    result_string += f"Параграф {paragraph_ind + 1}\n{par_string}\n"

        window = Toplevel()
        AnalyseResultFrame(window, result_string)


def main():
    from params import PARAMS

    root = Tk()
    ParamsInputFrame(root, param_ids=list(PARAMS.keys()))
    root.mainloop()


if __name__ == '__main__':
    main()
