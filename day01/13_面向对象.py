class Student:
    name = None;
    age = None;
    score = None;

    # __init__构造函数
    # self 代表类的实例本身,在java中用this标识
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return '姓名:%s,年龄:%d,成绩:%d' % (self.name, self.age, self.score)



stu1 = Student('张三', 18, 100)
print(stu1.name)
print(stu1.score)
print(stu1)
