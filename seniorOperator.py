"""
基于baseOperation (基本运算符) 进一步推出部分高级算符的函数，包括：
    * 三角函数
        ** sin/arcsin
        ** cos/arccos
        ** tan/arctan
        ** cot/arccot
    * 指数函数/幂函数

"""

from app.process.baseOperator import BaseOperator

class seniorOperation(BaseOperator):
    """
    高级运算符
    """
    def exponential(self):
        """
        幂函数
        """
        base = self.data1_getter()
        index = self.data2_getter()
        for i in range(index+1):
            ex = base * base
        return ex
    
    def sin_func(self):
        """
        sin函数
        """
        ans = 0
        return ans

    def cos_func(self):
        """
        cos函数
        """
        ans = 0
        return ans

    def tan_func(self):
        """
        tan函数
        """
        ans = 0
        return ans
"""
* for test

if __name__ == "__main__":
    ca = seniorOperation()
    ca.refresh_data_1(2)
    ca.refresh_data_2(2)
    print(ca.exponential())
"""



    
    