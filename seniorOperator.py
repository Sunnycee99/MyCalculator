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
        for i in range(1, num+1):
            ans = ans * i
        return ans

    def sin_func(self):
        """
        sin函数
        """
        num = self.data1_getter()
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
      
    def operation(self):
        """
        调用运算函数,并返回结果
        """
        if self.__operator_status == 1:
            return self.__add()
        elif self.__operator_status == 2:
            return self.__substract()
        elif self.__operator_status == 3:
            return self.__multi()
        elif self.__operator_status == 4:
            return self.__divide()
        elif self.__operator_status == 5:
            return self.sin_func()
        elif self.__operator_status == 6:
            return self.cos_func()
        elif self.__operator_status == 7:
            return self.tan_func()

"""
 for test
"""
"""
if __name__ == "__main__":
    ca = seniorOperation()
    ca.refresh_data_1(1.024)
    ca.refresh_data_2(-1)
    ca.refresh_status(3)
    print(ca.base_operation())
"""

    
    
