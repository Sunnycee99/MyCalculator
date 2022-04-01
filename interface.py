import PySimpleGUI as sg
from math import pi
from seniorOperator import seniorOperation
from baseOperator import BaseOperator
import re


def myfloat(x):
    if x != "pi":
        return float(x)
    else:
        return pi


def calculate(inputs):
    mybutton = lambda x: sg.B(x, size=(5, 1))
    layout = [
        [sg.Input(inputs, key="INPUT")],
        [mybutton(f"{i}") for i in range(7, 10)] + [mybutton("+")],
        [mybutton(f"{i}") for i in range(4, 7)]
        + [mybutton("-"), mybutton("sin"), mybutton("pi")],
        [mybutton(f"{i}") for i in range(1, 4)]
        + [mybutton("*"), mybutton("cos"), mybutton("C")],
        [
            mybutton("."),
            mybutton("0"),
            mybutton("="),
            mybutton("/"),
            mybutton("tan"),
            mybutton("L"),
        ],
    ]
    window = sg.Window("响存计算器", layout)
    so = seniorOperation()
    while 1:
        event, values = window.read()
        if event in (None, "Exit"):
            break
        if event == "=":
            content = window["INPUT"].get()
            try:
                operator = re.search("\+|\-|\*|/", content).group()
                data1, data2 = content.split(operator)
            except:
                breakpoint()
            if operator == "+":
                num = 1
            elif operator == "-":
                num = 2
            elif operator == "*":
                num = 3
            elif operator == "/":
                num = 4
            so.refresh_status(num)
            so.refresh_data_1(myfloat(data1))
            so.refresh_data_2(myfloat(data2))
            res = so.operation()
            window["INPUT"].update(myfloat(res))
            return res
        elif event == "C":
            so.clearData()
            window["INPUT"].update("")
        elif event == "L":
            content = window["INPUT"].get()
            window["INPUT"].update(content + so.ans_getter())
        else:
            if event in "sin":
                so.refresh_data_1(myfloat(window["INPUT"].get()))
                return so.sin_func()
            if event == "cos":
                so.refresh_data_1(myfloat(window["INPUT"].get()))
                return so.cos_func()
            if event == "tan":
                so.refresh_data_1(myfloat(window["INPUT"].get()))
                return so.tan_func()
            else:
                window["INPUT"].update(window["INPUT"].get() + event)
    window.close()


if __name__ == "__main__":
    res = calculate(0)
    sg.popup("结果为", res)
