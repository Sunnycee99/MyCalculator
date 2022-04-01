"""
基于baseOperation (基本运算符) 进一步推出部分高级算符的函数，包括：
    * 三角函数
        ** sin/arcsin
        ** cos/arccos
        ** tan/arctan
        ** cot/arccot
    * 指数函数/幂函数

"""

from baseOperator import BaseOperator

pi = 3.1415926


class seniorOperation(BaseOperator):
    """
    高级运算符
    """

    def exponential(self):
        """
        幂函数
        """
        self.__operator_status = 3
        base = self.data1_getter()
        index = self.data2_getter()
        ex = 1
        for i in range(index):
            ex = ex * base
        self.clearData()
        return ex

    def __factorial(self, num):
        """
        阶乘计算
        """
        ans = 1
        for i in range(1, num + 1):
            ans = ans * i
        return ans

    def sin_func(self):
        """
        sin函数
        """
        num = self.data1_getter()
        k = num // (2 * pi)
        num = num - 2 * pi * k
        if num > pi:
            num = pi - num
        ans = 0.0
        for i in range(1, 13, 4):
            self.refresh_data_1(num)
            self.refresh_data_2(i)
            ans = ans + (self.exponential() / self.__factorial(i))
            self.clearData()
        for i in range(3, 15, 4):
            self.refresh_data_1(num)
            self.refresh_data_2(i)
            ans = ans - (self.exponential() / self.__factorial(i))
            self.clearData()
        return ans

    def cos_func(self):
        """
        cos函数
        """
        ans = 0.0
        num = self.data1_getter()
        k = num // (2 * pi)
        num = num - 2 * pi * k
        if num > pi:
            num = 2 * pi - num
        for i in range(0, 12, 4):
            self.refresh_data_1(num)
            self.refresh_data_2(i)
            ans = ans + (self.exponential() / self.__factorial(i))
            self.clearData()
        for i in range(2, 14, 4):
            self.refresh_data_1(num)
            self.refresh_data_2(i)
            ans = ans - (self.exponential() / self.__factorial(i))
            self.clearData()
        return ans

    def tan_func(self):
        """
        tan函数
        """
        ans = 0.0
        num = self.data1_getter()
        sin_ans = self.sin_func()
        self.refresh_data_1(num)
        cos_ans = self.cos_func()
        ans = sin_ans / cos_ans
        return ans


"""
 for test
"""
if __name__ == "__main__":
    ca = seniorOperation()
    from math import pi

    ca.refresh_data_1(4.14)
    ca.refresh_data_2(-1)
    ca.refresh_status(3)
    print(ca.operation())
    print(ca.sin_func())
    ca.refresh_data_1(4.14)
    ca.refresh_data_2(-1)
    ca.refresh_status(3)
    print(ca.cos_func())
