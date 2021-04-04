from tkinter import Tk, Toplevel, filedialog, StringVar, LabelFrame
from tkinter.ttk import Frame, Button, Label, Entry, Radiobutton, Combobox
from tkinter import BOTH, TOP, W, LEFT, N, X, Y, E, BOTTOM, S

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

        main_container = Frame(self)
        main_container.pack(fill=BOTH)

        self.left_container = Frame(main_container)
        self.right_container = AnalyseResultFrame(main_container)

        self.left_container.pack(side=LEFT, anchor=W)
        self.right_container.pack(side=LEFT)

        params_container = Frame(self.left_container)

        __params = list(PARAMS.values())
        p = {
            'Шрифты': __params[:5],
            'Абзац': __params[5:],
        }

        for category_name, params in p.items():
            group = LabelFrame(params_container, text=category_name)
            group.pack(side=TOP, fill=X)

            #_create_group_params(group, params)

            for param in params:
                param_id = 0
                for id_, _parameter in PARAMS.items():
                    if param == _parameter:
                        param_id = id_
                inner_container = Frame(group)
                lbl = Label(inner_container, text=param.name)
                text_field = Combobox(inner_container,
                                      textvariable=self.user_input[param_id])
                text_field['values'] = param.default_vals
                text_field.current(param.start_val)

                lbl.pack(side=LEFT, anchor=W)
                text_field.pack(side=LEFT, expand=True, anchor=E)

                inner_container.pack(side=TOP, fill=X, padx=10)


#        group = LabelFrame(params_container, text='Шрифт')
#        group.pack(side=TOP, fill=X)
#
#        group2 = LabelFrame(params_container, text='Абзац')
#        group2.pack(side=TOP, fill=X)
#
#        indent = 0
#        i = 0
#        for param_id in self.param_ids:
#            param = PARAMS[param_id]
#            if i < 4:
#                current_group = group
#            else:
#                current_group = group2
#            inner_container = Frame(current_group)
#            lbl = Label(inner_container, text=param.name)
#            text_field = Combobox(inner_container,
#                                  textvariable=self.user_input[param_id])
#            text_field['values'] = param.default_vals
#            text_field.current(param.start_val)
#
#            lbl.pack(side=LEFT, anchor=W)
#            text_field.pack(side=LEFT, expand=True, anchor=E)
#
#            inner_container.pack(side=TOP, fill=X, padx=10)
#            i += 1

        self.addButton = Button(self.left_container,
                                text="Начать анализ",
                                command=self.new_test)

        params_container.pack(side=TOP, fill=BOTH)
        self.addButton.pack(side=TOP, pady=8)


    def centerWindow(self):
        w = 840
        h = 410
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
            for paragraph_ind, paragraph in enumerate(doc.paragraphs):
                formatting = paragraph.paragraph_format
                par_string = ""
                for param_id in self.paragraph_params:
                    param = PARAMS[param_id]
                    #print(f"Analyzing param {param.name}")
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

#        window = Toplevel()
#        AnalyseResultFrame(window, result_string)
        self.right_container.set_text(result_string)


def main():
    from params import PARAMS

    root = Tk()
    ParamsInputFrame(root, param_ids=list(PARAMS.keys()))
    root.mainloop()


if __name__ == '__main__':
    main()

