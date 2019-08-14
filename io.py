'''
文件打开方式
'''
# file_object = open("test.txt","r")#只读，要求文件存在
# file_object = open("test.txt","w")#只写，文件不存在就创建，存在则清空
# file_object = open("test.txt","a")#只写，文件不存在就创建，存在则追加
# file_object = open("test.txt","r+")#读写，文件不存在就创建，存在则追加
# file_object = open("test.txt","w+")#读写，文件不存在就创建，存在则追加
# file_object = open("test.txt","a+")#读写，文件不存在就创建，存在则追加

# file_object = open("test.txt","rb")#加b后续的读写都以字节串操作

'''
所有文件都可以用二进制方式打开（b）
但是二进制格式文件则不能用文本方式打开（后续读写出错）
'''
# file_object=open("pic.jpg","r")

'''
文件读取
'''
# #打开文件
# file_object=open("test.py","r")
# #读取文件
# data=file_object.read(100)
# print(data)

# #循环读取文件内容
# while True:
#     #如果读到文件结尾read（）会读到空字符串
#     data=file_object.read(1024)
#     #读到结尾跳出循环
#     if not data:
#         break
#     print(data)

# #用来读取文件中一行
# data=file_object.readline(10)
# print(data)
# data=file_object.readline(15)
# print(data)

# #用来读取文件中的每一行作为列表中的一项（返回一个列表）
# data=file_object.readlines(40)
# print(data)

# #文件对象也是可迭代对象，可以用for读取文件每一行
# for i in file_object:
#     print(i)#每次迭代到一行内容

'''
练习：编写一个程序，从终端输入一个单词，可以打印出单词及其解释
    如果没有这个单词则打印“没有该单词”
'''
# while True:
#     with open("dict.txt") as file_object:
#         word=str(input("请输入单词："))
#         for i in file_object:
#             if i.find(word)==0:
#                 print(i)
#                 break
#         else:print('没有该单词')

# while True:
#     with open("dict.txt") as file_object:
#         word=str(input("请输入单词："))
#         for i in file_object:
#             w=i.split(" ")[0]
#             if w > word:
#                 print("没有该单词")
#                 break
#             if w==word:
#                 print(i)
#                 break
#         else:print('没有该单词')

'''
文件写操作
'''
# f=open("pic.jpg","a")
# #写操作
# f.write("print('我：hello world')\n")
# f.write("print('world：干哈？')")
# f.close()

'''
练习：将一个文件（可能是文本也可能是二进制文件）拷贝一份
    test.jpg-->test-bak.jpg
'''
# f=open("pic.jpg","rb+")
# r=open("pic-bak.jpg","wb")
# r.write(f.read())

# filename=input("filename:")
# try:
#     fr=open(filename,'rb')
# except FileNotFoundError as e:
#     print(e)
# else:
#     newname=input("newname:")
#     fw=open(newname,"wb")
#     while True:
#         item=fr.read(1024)
#         fw.write(item)
#         if not item:
#             break

'''
缓冲区刷新测试
'''
# f=open("test.py","w")
# while True:
#     data=input(">>")
#     if not data:
#         break
#     f.write(data)
#     f.flush()
# f.close()

'''
文件偏移量
'''
# f=open("test.py","ab+")
# f.seek(-10,0)
# f.write("你好".encode())
# f.close()

'''
空洞文件
'''
# f=open('test','wb')
# f.write(b"start")
# f.seek(1024*1024)
# f.write(b"end")
# f.close()

'''
文件管理函数
'''
# import os
# #获取文件大小
# print(os.path.getsize("pic.jpg"))
#
# # 看文件列表
# #print(os.listdir())
#
# #查看文件是否存在
# print(os.path.exists("pic.jpg"))
#
# #判断文件类型
# print(os.path.isfile("pic.jpg"))
#
# #删除文件
# os.remove("test.txt")

'''
osi七层模型
'''