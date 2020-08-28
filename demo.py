# print("xixi",end = "")
# print(2)
# print(2.33)
# print(True,False)
# print(())
# print([])
# print({})
# print(None)
# print("haha"+"1")
# print("haha","xixi",123,False)

# a = input("请输入第一个数字：")
# b = input("请输入第二个数字：")
# print(int(a)+int(b))
# print(type(int(a)+int(b)))

# c = int("1")
# print(type(c))

# print(len("哈哈"))
# """
# 使用python来实现一个，计算用户输入的文章的字数的功能
# """
# article = input("请编写你的文章：")
# article_num = len(article)
# print(article_num)

#元组的作用是用来装数据的
#每个变量都是存在内存中的
#每个放到元组里的数据，电脑都会给它自动编号，这个标号就叫 下标
#计算机整数都是从0开始的
# a = (1,2,3,"4",True) #定义了一个a变量，把空的元组赋值给了a
# print(a[0])
# print(a[-3])
# print(a.count(3))
# print(a.index(3))

# b = (a,"haha",("haha","xixi"))
# print(b[0][1])
# print(b[2].index("xixi"))

#数组和元组的操作是一模一样的
#数组和元组的区别：元组不可以修改；数组可以修改
a = [1,1,1,3,5,"haha","haha"]
print(a.index(1))
print(a.count(1))
a.append("插入的内容")
print(a)
a.extend("1111")
print(a)

