# 用python实现Cat类，Cat有name，有age/性别，Cat可以叫，成员方法打印一句话即可。然后实例化这个Cat类，去调用name/age/叫方法
# class  Cat():
#     name = "coco"
#     age = "2"
#     sex = "girl"

#     def call(self,something,drink):
#         print("coco会叫{}！还可以喝{}！！".format(something,drink))

# c = Cat()
# print(c.name,c.age)
# c.call("xixi","water")

class Father():
    name = "mayun"
    money = "500e"

    def make_monkey(self):
        self.yanzhi = "帅气"      #类新增成员变量
        print("{}可以赚大钱".format(self.name))

    def use_monkey(self):
        print("马爸爸挥金如土")

a = Father()
a.make_monkey()
print(a.yanzhi)