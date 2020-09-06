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
# a = [1,1,1,3,5,"haha","haha"]
# print(a.index(1))
# print(a.count(1))
# a.append("插入的内容")
# print(a)
# a.extend("1111")
# print(a)
# a.insert(0,"wyt")
# print(a)
# # a.sort()
# # print(a)
# a.remove(5)
# print(a)

#字典没有下标的概念
# a = {
#     "name":"wyt",
#     "age":19,
#     "address":"fujian",
#     "info":{
#         "boyfrined":["one","two","three"],
#         "girlfriend":(1,2,3,4)
#        },
# }
# print(a["info"])
# print(a.get("info1"))
# print(list(a.keys()))
# print(list(a.values()))
# print(a.items())
# a.update(name1 = "wyt1")
# print(a)
# x = a.pop("name1")
# print(a)
# a["name2"] = "wyt2"
# a["name1"] = "wyt11"
# print(a)

#通过python实现一个自动录入成绩的程序，输入学生的名字和成绩，然后成对的储存到变量中。
# 输入结束后，打印出结果。
# sName = input("请输入学生的姓名：")
# sScore = int(input("请输入学生的成绩："))
# sNameScore = {sName:sScore}
# print(sNameScore)

# sNameScore = {}
# sName = input("请输入学生的姓名：")
# sScore = int(input("请输入学生的成绩："))
# sNameScore[sName] = sScore
# print(sNameScore)

'''
判断
1.if
2.if ... else ...
3.if ... elif ... else
如果 条件
那么 动作
'''
# age = int(input("请输入你的年龄："))
# if age > 65:
#     print("你要退休啦！")
# elif age >30:
#     print("继续加油努力赚钱！")
# elif age>20:
#     print("继续加油吧")
# else:
#     print("你还小")

'''
3.使用python实现一个登录功能
'''
# realzhanghao = "15659658891"
# realmima = "123456"
# zhanghao = input("请您输入您的账号：")
# mima = input("请您输入您的密码：")
# if zhanghao == realzhanghao and mima == realmima:
#     print("登录成功")
# elif zhanghao != realzhanghao:
#     print("当前账号不存在，请输入正确账号!")
# else:
#     print("密码有误，请重新输入")

'''
4.使用python来实现一个注册的功能，要求账号必须大于5位，密码大于8位。
'''
# userinfo = {}
# username = input("请您输入账号：")
# password = input("请您输入密码：")
# if len(username) > 5:
#     if len(password) > 8:
#         userinfo["username"] = username
#         userinfo["password"] = password
#         print("注册成功！")
#     else:
#         print("请输入大于8位的密码！")
# else:
#     print("请输入大于5位的账号！")
# print(userinfo)

'''
for循环是通过遍历的方式实现的
也就是说，遍历的对象里面有多少个值，那么for循环下面的代码，就会运行多少次！

在循环里面，遇到了break就结束当前循环，如果遇到了continue，那后面的代码就不会运行了，继续下一次循环。
'''
# for i in "今天你吃了么？":
#     print(i)

'''
5.使用python打印出一个99乘法表
'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",i*j,end="  ")
#     print()

'''
6.使用代码实现一个1-100的累加
'''

# sum = 0
# n = 1
# while n <= 100:
#     sum =sum + n
#     n = n + 1
# print(sum)

'''
7.现在有一堆成绩，请把及格的和不及格的分别放到不同的数组中。
数据如下：[{"tom":98,"king":56,"lili":75}]
'''
score = [{"tom":98,"king":56,"lili":75}]
scorepass = [{}]
scorefail = [{}]
sdict = score[0]
for i in score[0]:
    if score[0][i] >= 60:
        scorepass[0][i] = score[0][i]
    else:
        scorefail[0][i] = score[0][i]
print(scorepass)
print(scorefail)
'''
8.使用python的print，模拟一个红绿灯的功能
'''
redgree = {"红灯":30,"绿灯":15,"黄灯":5}
for i in redgree:
    for j in range(redgree[i],0,-1):
        print(i,"还有",j,"秒")

'''
9.实现一个注册功能，要求账号5-8位，并且小写字母开头，不允许符号，仅小写字母和数字组成。
密码8-12位，并且密码必须包含3种字符串，比如aaa123!
'''