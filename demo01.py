'''
异常处理:即使代码报错，还要继续运行
'''

try:
    a = [1,2,3,4]
    a[-100]
    print("1")
except:
    print("2")

print("3")