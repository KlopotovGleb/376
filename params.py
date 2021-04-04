class Parameter:
    def __init__(self, name: str, is_run: bool, is_boolean: bool, getter, default_vals=None, start_val=None):
        self.name = name
        self.is_run = is_run
        self.getter = getter
        self.is_boolean = is_boolean
        self.id = -1
#        if not is_boolean:
#            assert default_vals is not None
        self.default_vals = default_vals
        self.start_val = start_val

        self.current_value = None

    def get_value(self, data):
        return self.getter(data)

    def get_current_value(self):
        return self.current_value

    def __str__(self):
        return f"Parameter({self.name})"

    def __repr__(self):
        return f"Parameter({self.name})"


def safe_get_cm(length):
    return length.cm if length is not None else 0.


def safe_get_pt(length):
    return length.pt if length is not None else 0.


def get_bool(bool_val):
    return "Да" if bool_val else "Нет"


all_params = [
    Parameter(
        name="Шрифт",
        is_run=True,
        is_boolean=False,
        getter=lambda run: run.font.name,
        default_vals=('Times New Roman', 'Calibri'),
        start_val=0
    ),
    Parameter(
        name="Размер шрифта",
        is_run=True,
        is_boolean=False,
        getter=lambda run: safe_get_pt(run.font.size),
        default_vals=(1., 2., 3., 4., 6., 8., 9., 10., 11., 12., 14., 16., 18.),
        start_val=10
    ),
    Parameter(
        name="Курсивный текст",
        is_run=True,
        is_boolean=True,
        default_vals=('Да', 'Нет'),
        start_val=1,
        getter=lambda run: get_bool(run.italic)
    ),
    Parameter(
        name="Подчёркнутый текст",
        is_run=True,
        is_boolean=True,
        default_vals=('Да', 'Нет'),
        start_val=1,
        getter=lambda run: get_bool(run.underline)
    ),
    Parameter(
        name="Выравнивание абзаца",
        is_run=False,
        is_boolean=False,
        getter=lambda formatting: formatting.alignment,
        default_vals=("LEFT (0)", "RIGHT (0)"),
        start_val=0
    ),
    Parameter(
        name="Отступ перед абзацем",
        is_run=False,
        is_boolean=False,
        getter=lambda formatting: safe_get_cm(formatting.space_before),
        default_vals=(0., 1., 2., 3., 4.),
        start_val=0
    ),
    Parameter(
        name="Отступ после абзаца",
        is_run=False,
        is_boolean=False,
        getter=lambda formatting: safe_get_cm(formatting.space_after),
        default_vals=(0., 1., 2., 3., 4.),
        start_val=0
    ),
    Parameter(
        name="Отступ слева",
        is_run=False,
        is_boolean=False,
        getter=lambda formatting: safe_get_cm(formatting.left_indent),
        default_vals=(0., 1., 2., 3., 4.),
        start_val=0
    ),
    Parameter(
        name="Отступ справа",
        is_run=False,
        is_boolean=False,
        getter=lambda formatting: safe_get_cm(formatting.right_indent),
        default_vals=(0., 1., 2., 3., 4.),
        start_val=0
    ),
    Parameter(
        name="Отступ первой строки абзаца",
        is_run=False,
        is_boolean=False,
        getter=lambda formatting: safe_get_cm(formatting.first_line_indent),
        default_vals=(0., 1., 2., 3., 4.),
        start_val=0
    ),
    Parameter(
        name="Не отрывать от следующего абзаца",
        is_run=False,
        is_boolean=True,
        default_vals=('Да', 'Нет'),
        start_val=0,
        getter=lambda formatting: get_bool(formatting.keep_with_next)
    ),
    Parameter(
        name="Не разрывать абзац",
        is_run=False,
        is_boolean=True,
        default_vals=('Да', 'Нет'),
        start_val=0,
        getter=lambda formatting: get_bool(formatting.keep_together)
    ),
]

PARAMS = {}

for param_id, elem in enumerate(all_params):
    PARAMS[param_id] = elem
    elem.id = param_id

