import os
from input_output import get_input, get_output
from math import acos, asin, atan, sin, cos, tan, pi
from interface import calculate

os.chdir(os.path.dirname(__file__))
if __name__ == "__main__":
    inputs = get_input()  # 从input.txt读取数字
    res = calculate(inputs)  # 从界面计算
    get_output(res)  # 返回计算结果
