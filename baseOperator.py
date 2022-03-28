"""
base operation model
"""


class BaseOperator:
    """
    基础运算符模型，存放基本的加减乘除运算
    0: 无操作
    1: 相加
    2: 相减
    3: 相乘
    4: 相除
    """
    __operator_status = 0   # 私有变量，表示当前需进行的运算操作
    __data_1 = 0
    __data_2 = 0


    def __add(self):
        """
        两数相加
        """
        return self.__data_1 + self.__data_2

    def __substract(self):
        """
        两数相减
        """
        return self.__data_1 - self.__data_2

    def __multi(self):
        """
        两数相乘
        """
        return self.__data_1 * self.__data_2
        
    def refresh_data_1(new_data, self):
        """
        data_1赋值
        """
        self.__data_1 = new_data

    def refresh_data_2(new_data, self):
        """
        data_2赋值
        """
        self.__data_2 = new_data

    def refresh_status(new_status, self):
        """
        操作私有变量operator_status
        """
        self.__operator_status = new_status

    def base_operation(self):
        """
        调用运算函数,并返回结果
        """
        if self.__operator_status == 1:
            self.__add(self.__data_1, self.__data_2)
        elif self.__operator_status == 2:
            self.__substract(self.__data_1, self.__data_2)
        elif self.__operator_status == 3:
            self.__multi(self.__data_1, self.__data_2)
        


    
    
