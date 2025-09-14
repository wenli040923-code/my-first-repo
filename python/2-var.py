# # 驼峰命名法
# person_name = "罗文丽"
# MAX_NUM = 1024

# def get_name():
#     return "罗文丽"

# # 第一个注释
# """ 第二个注释 """

# def add(a : int, b : int) -> int:
#     """
#     Args:
#         a: int 第一个数
#         b: int 第二个数
#     Return:
#         int 对应a+b的结果
#     """
#     # 强烈要求a和b是整形
#     if type(a) != type(1) or type(b) != type(1):
#         # 抛出错误
#         raise "a和b不是整形"
#     # 返回
#     return int(a) + int(b)

# # 我们给变量a一个类型声明
# a1: int = 1.1
# # 变量会自己推断自己的类型
# a2 = 2
# # add(a1, a2)
# print(type(a1))

# # 隐式转换
# a1: int = int(1.1)
# print(a1)
# print(type(a1))

# # round函数会四舍五入
# print(round(1.546678527, 6))

# b = 1e-6 # 1 * 10^6

# # 自动推断
# b = 2
# print(type(b))
# b = 2.2
# print(type(b))
# b = {
#     1: 2
# }
# print(type(b))

# flag = None # None类型
# print(type(flag))

# str1 = "罗文丽"
# str2 = '罗文丽'
# str3 = """
# 罗文丽
# 你好，我爱你
# """
# print(str1)
# print(str2)
# print(str3)


# name = "罗" + "文" + "丽"
# say = "我爱你！"*100

# print(name)
# print(say)

# str4 = "name:罗文丽, say:我爱你" # 非ASCII码

# result_str = str()

# # print(chr(65))
# # print(ord("A"))
# # 可迭代对象 --> 连续的类型 字符串，元组，列表，字典
# # for i in 可迭代对象
# for s in str4:
#     t = ord(s)
#     if t >= 0 and t < 128:
#         result_str += s
        
# # print(result_str)
# # print(str4[-2])
# # print(str4[15])
# # Python字符串不能改变！！！
# # str4[0] = "N"
# # print(str4)
# C语言写法
# for index in range(len(str4)):
#     print(str4[index])

# str5 = "罗文丽我爱你"
# str6 = "0123456789"

# 有很多科学计算方法 -> 底层是C语言 -> 做人工智能
# import numpy as np

# list1 = np.array([[1, 2, 3], 
#         [4, 5, 6]])

# print(type(list1))

# # 切片
# print(str5[0:3])
# # 默认值 start = 0, end = 长度 + 1, step = 1
# print(str6[::2])
# print(str6[1::2])

# # 进阶切片  -》 numpy
# print(list1[1::,1::]) # -> 5 6

# name = "罗文丽"

# say = input("")

# print(say)


# num1 = int(input())

# result =num1 + 2

# print(result)

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 不可修改
str1 = "你好我爱你罗文丽"
# 可修改的数组 -> 里面的元素可以是任何类型
list1 = [1, 2, "A"]
# 不可修改的数组
tuple1 = (1, 2, "A")
# 字典类型
dict1 = {
    1: "罗文丽",
    2: "程耀宇"
}
# 集合类型
set1 = {1, 1, 2, 3}

# for i in dict1.keys():
#     print(i)
# print(list1)
# list1[0] = 2
# print(list1)

# print(str1)
# print(list1)
# print(tuple1)
# print(dict1)
# print(set1)

# name = "罗文丽"
# say = "我爱你"
# number = 1314
# # 字符串的格式化方式
# # 第一种格式化打印的方式 --> 最常用的
# result_str = f"我想说的是，{name},{say}{number}!"
# # 第二种方式 --> 基本不用的
# result_str = "我想说的是，%s,%s%s!" % (name, say, number)
# print(result_str)

# 第一种导入
# import test

# test.my_say()

# test.name="程耀宇"

# test.my_say()

# name = "lwl"

# # 第二种导入方式
# from test import say, name, my_say

# print(name)

# 第三种导入方式
# from test import my_say as m_s
# m_s()
# import my_module
# from my_module import test
# my_module.test.my_say()

# # 第四种导入方式
# from my_module.test import my_say, name, say
# my_say()

# 运行一个开源项目必须要做的步骤
# 导入pygame
# import pygame
# print(pygame)

# 切片 --> 非常常用
work_str = "我喜欢罗文丽宝宝，最爱罗文丽宝宝啦！"
print(work_str[::-1])
# 反转
# 切片[start:end:step]  start = 0, end = len(str) + 1, step = 1

# 字符串格式化方式
name = "罗文丽"
say = "我爱你"

result_str = f"{name},{say}"
# 基本不常用
result_str = "%s,%s!" % (name, say)
print(result_str)

# 导包 pandas
import pandas
# 导入pandas里面的to_csv方法
from pandas import to_csv