def add(a,b):
    return a+b;

def my_print():
    print("hello world");
def myDef():
    return 1,2,"ABC"


addResult = add(3,5);
print("addResult = ", addResult);
my_print();
#在python中，方法是可以有多个返回值的
a,b,c= myDef()
print(a,b,c)
