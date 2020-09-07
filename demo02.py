#def : 关键字
#方法名字 ： 不能以特殊符号和数字开头，用小写的字母开头

def add(a1=10,a2=20): #a1,a2有默认值
    sum = a1 + a2
    return sum
s1 = add(11)
print(s1)
