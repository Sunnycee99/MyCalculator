import PySimpleGUI as sg
from math import acos, asin, atan, sin, cos, tan, pi


def calculate(inputs):
    mybutton = lambda x: sg.B(x, size=(5, 1))
    layout = [
        [sg.Input(inputs, key="INPUT")],
        [mybutton(f"{i}") for i in range(7, 10)]
        + [mybutton("+"), mybutton("("), mybutton(")"), mybutton("^")],
        [mybutton(f"{i}") for i in range(4, 7)]
        + [mybutton("-"), mybutton("sin"), mybutton("asin"), mybutton("pi")],
        [mybutton(f"{i}") for i in range(1, 4)]
        + [mybutton("*"), mybutton("cos"), mybutton("acos"), mybutton("D")],
        [
            mybutton("."),
            mybutton("0"),
            mybutton("="),
            mybutton("/"),
            mybutton("tan"),
            mybutton("atan"),
            mybutton("C")
        ],
    ]
    window = sg.Window("响存计算器", layout)
    while 1:
        event, values = window.read()
        if event in (None, "Exit"):
            break
        if event == "C":
            try:
                return str(eval(window["INPUT"].get()))
            except ValueError as ex:
                sg.popup(ex + ",请检查输入")
        elif event == "D":
            window["INPUT"].update(window["INPUT"].get()[:-1])
        else:
            window["INPUT"].update(window["INPUT"].get() + event)
    window.close()
