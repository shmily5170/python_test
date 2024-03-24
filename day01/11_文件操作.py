#在Python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下
#open("文件名", "文件操作方式", "encoding:编码格式（推荐使用UTF-8");
file = open("新建文本文档.txt",encoding="UTF-8");
context= file.read()
file.close();
print(context)

print("--------------------------")
# 1. 打开文件 如果是w会清空原来的文件写入，如果是a则不会清空原来的文件，向后追加
f = open('python.txt', 'w')
# 2.文件写入
f.write('hello world')
# 3. 内容刷新,数据刷新后才会真正的写入硬盘
f.flush()



