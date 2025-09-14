
# Python 能够自己推断类型 低精度->高精度
counter = 100 * 1.0
miles = 170.0
name = "罗文丽"
ratio = 2/1 
# python 低精度 -> 高精度 -> 防止精度丢失

print(ratio)

# 多变量肤质
a = b = c = 1

a = 2
b = 1

# # 交换算法
# t = a 
# a = b 
# b = t
# print(a, b)

# 同时进行
# a,b = b,a 
# print(a, b)

# import numpy

# print(numpy)

# # 有个变量，我想判断它是否是浮点型，应该怎么写？

# from test import X

# # 判断X是不是浮点类型

# if type(X) == type(float()):
#     print("是浮点类型")
# else:
#     print("不是浮点型")


# num1 = 4 + 3j
# num2 = 3 - 4j

# print(num1 + num2)
# print(type(num1))

# isinstance -> 判断
from test import X
if isinstance(X, float):
    print("浮点类型")


class A:
    pass

class B(A):
    pass

print(type(B()) == type(A()))
print(isinstance(A(),B))

# 初始化 -> 初始 
# str3 = str()

# print(type(B))
# print(type(B()))
# print(type(A()))

# import numpy
# print(type(float()))

# str4 = str
# print(type(str4))
# # 初始化
# str_result = str4() # str_result = str()
# print(type(str_result))                   