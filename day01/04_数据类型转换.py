#定义一个字符串，将其转换成int与float
str1 = '123'
convertInt = int(str1)
converFloat = float(str1)

# 浮点数转整数是向下取整
intNumber = int(13.567);
print(type(intNumber), intNumber);

#请注意，在python中，如果需要将字符串与其他数据类型进行打印，需要将其他数据类型一起转化成字符串，不然会报错
name = 'ABCD';
number = 123456789;
float1 = 123456.789
print("这是一串字符串:" + name + '，这是一串数字：' + str(number));

#%s是字符串占位，%d是整数数字占位，%f是浮点数占位
print("这是一串字符串:%s，这是一串数字：%s"  %(name, number));

#快速字符串格式化，在字符串前面加f，后面跟{}，{}中填入变量名
print(f"这是一串字符串:{name}，这是一串数字：{number},这是一串浮点数：{float1}");

