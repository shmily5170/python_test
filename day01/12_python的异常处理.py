import time

try:
    #可能出现异常的代码块
    f = open('linux.txt', 'r')
    time.sleep(1)
except Exception as e:
    #如果出现异常，执行except的代码
    f = open('linux.txt', 'w')
finally:
    f.close()

