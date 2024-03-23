import time

"""
数字（Number）：
Python支持整数（int）、浮点数（float）、复数（complex）等数字类型。
整数使用10、123等表示。
浮点数使用10.0、3.14等表示。
复数使用1+2j等表示。
"""
print(10);
print(10.0);
print(1+2j);
print(True)
print("---------------")
"""
字符串（String）：
Python中的字符串使用单引号' '或双引号" "括起来表示。
字符串支持多种操作，如拼接、切片、索引等。
"""
print("Hello World");
print("---------------")
"""
列表（List）：
列表是Python中一种有序的数据结构，可以包含不同类型的元素。
列表使用方括号[]括起来，元素之间使用逗号分隔。
列表支持多种操作，如索引、切片、拼接、排序等。
"""
my_list = [1, 2, 3, 4, 5];
print(my_list);
print(type(my_list))
print("---------------")

"""
组（Tuple）：
元组是Python中另一种有序的数据结构，与列表类似，但元组是不可变的。
元组使用圆括号()括起来，元素之间使用逗号分隔。
"""
my_tuple = (1, 2, 3, 'Hello', 4.5);
print(my_tuple);
print("---------------")
"""
字典（Dictionary）：
字典是Python中一种无序、可变的数据结构，由键值对组成。
字典使用大括号{}或dict()函数创建
"""
my_dict = {'name': 'Tom', 'age': 20, 'city': 'Shanghai'};
print(my_dict);

