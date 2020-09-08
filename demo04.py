class Person():
    name = "小小王" #成员变量-->类的变量:属性
    age = 18
    sex = "boy"

    # 成员方法
    # self:固定的用法
    def eat(self):
        print("人可以吃饭！")

# 类的调用：实例化类,p类的实例化对象，类的把柄
p = Person()
print(p.age)
p.eat()