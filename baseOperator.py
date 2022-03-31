"""
Create by LYL
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
    __operator_status = None   # 私有变量，表示当前需进行的运算操作
    __data_1 = None
    __data_2 = None
    __saved_ans = None

    def __add(self):
        """
        两数相加
        """
        ans = self.__data_1 + self.__data_2
        self.ans_setter(ans)
        return 

    def __substract(self):
        """
        两数相减
        """
        ans = self.__data_1 - self.__data_2
        self.ans_setter(ans)
        return ans

    def __multi(self):
        """
        两数相乘
        """
        ans = self.__data_1 * self.__data_2
        self.ans_setter(ans)
        return ans
    
    def __divide(self):
        """
        两数相除
        """
        ans = self.__data_1 / self.__data_2
        self.ans_setter(ans)
        return ans
        
    def refresh_data_1(self, new_data):
        """
        data_1赋值
        """
        self.__data_1 = new_data

    def data1_getter(self):
        """
        获取data1
        """
        return self.__data_1

    def refresh_data_2(self, new_data):
        """
        data_2赋值
        """
        self.__data_2 = new_data

    def data2_getter(self):
        """
        获取data2
        """
        return self.__data_2

    def refresh_status(self, new_status):
        """
        操作私有变量operator_status
        """
        self.__operator_status = new_status
    
    def ans_setter(self, new_ans):
        """
        存储计算结果
        """
        self.__saved_ans = new_ans

    def ans_getter(self):
        """
        取出上一次计算的结果
        """
        return self.__saved_ans

    def clearData(self):
        """
        清除数据
        """
        self.refresh_data_1(None)
        self.refresh_data_2(None)
        self.refresh_status(None)
        self.ans_setter(None)

    def base_operation(self):
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

