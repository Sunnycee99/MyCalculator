import PySimpleGUI as sg
from math import acos, asin, atan, sin, cos, tan, pi


class seniorOperator:
    def __init__(self, window):
        self.window = window
        self.content = ""

    def clearData(self):
        self.window["INPUT"].update("")

    def add_number(self, number):
        window = self.window
        self.window["INPUT"].update(window["INPUT"].get() + number)
        self.content = self.content + number

    def add_operator(self, operator):
        window = self.window
        self.window["INPUT"].update(window["INPUT"].get() + operator)
        self.content = self.content + operator

    def add_function(self, function):
        window = self.window
        self.window["INPUT"].update(window["INPUT"].get() + function)
        self.content = self.content + function

    def operation(self):
        try:
            return str(eval(self.window["INPUT"].get()))
        except ValueError as ex:
            print(ex + ",请检查输入")


def calculate(inputs):
    mybutton = lambda x: sg.B(x, size=(5, 1))
    layout = [
        [sg.Input(inputs, key="INPUT")],
        [mybutton(f"{i}") for i in range(7, 10)]
        + [mybutton("+"), mybutton("("), mybutton(")"), mybutton("^")],
        [mybutton(f"{i}") for i in range(4, 7)]
        + [mybutton("-"), mybutton("sin"), mybutton("asin"), mybutton("pi")],
        [mybutton(f"{i}") for i in range(1, 4)]
        + [mybutton("*"), mybutton("cos"), mybutton("acos"), mybutton("C")],
        [
            mybutton("."),
            mybutton("0"),
            mybutton("="),
            mybutton("/"),
            mybutton("tan"),
            mybutton("atan"),
        ],
    ]
    window = sg.Window("响存计算器", layout)
    ca = seniorOperator(window)
    while 1:
        event, values = window.read()
        if event in (None, "Exit"):
            break
        if event == "=":
            return ca.operation()
        elif event == "C":
            ca.clearData()
        elif event == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            ca.add_number(event)
        elif event == ["+", "-", "*", "/", "(", ")"]:
            ca.add_operator(event)
        else:
            ca.add_function(event)  # 添加类似sin，cos这样的函数

    window.close()


if __name__ == "__main__":
    res = calculate(0)
    sg.popup("结果为", res)
