# list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)
#list(列表) / 数组
list1 = [1, 2, 3, 4, 5];
print('A' in list1) # 判断元素是否存在
"""
list1.append(6) # 添加元素
list1.insert(0, 0) # 插入元素
list1.remove(1) # 删除元素1
list1.pop() # 删除最后一个元素
list1.pop(0) # 删除第一个元素
list1.clear() # 清空列表
list1.sort() # 列表排序
list1.reverse() # 列表反转
list1.count(1) # 统计元素1的个数
list1.index(1) # 查找元素索引,如果查找的元素不存在，会报错,可以使用 1 in list1 的方式确定以下元素是否存在
list1.extend([6, 7, 8]) # 添加多个
"""
#tuple(元组)，元组里面的数据被定义后就不可以被修改，地址不可变，不是内容不可变
tuple1 = (1, 2, 3, 4, 5);
print('A' in tuple1)
"""
tuple1.count(1) # 统计元素1的个数
tuple1.index(1) # 查找元素索引,如果查找的元素不存在，会报错,可以使用 1 in tuple1 的方式确定以下元素是否存在
"""
#str(字符串)
str1 = 'hello world'
"""
相关方法和使用请看这个，和java差不多
https://blog.csdn.net/qq_43704782/article/details/123241359
"""
#set(集合)
set1 = {1, 2, 3, 4, 5}
"""
set1.add(6) # 添加元素
set1.remove(1) # 删除元素1
set1.clear() # 清空集合
set1.pop() # 删除第一个元素
set1.union(set2) # 合并两个集合
set1.intersection(set2) # 求交集
set1.difference(set2) # 求差集
set1.symmetric_difference(set2) # 求对称差集
set1.issubset(set2) # 判断set1是否是set2的子集
"""
#dict(字典)
dict1 = {'name': 'zhangsan', 'age': 18}
"""
字典常用函数
https://blog.csdn.net/qq_41917061/article/details/119180308
"""
