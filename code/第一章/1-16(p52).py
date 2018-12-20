class First:								#定义父类
    fir = 111
    def __init__(self):
        print("Uses the first function.")
	def check1(self):
        print("Method of the first function.")

class Second(First):							#定义子类
    sec = 222
    def __init__(self):
        print("Uses the second function.")
    def check2(self):
        print("Method of the second function.")

f = First()									#用父类申明对象f
s = Second()								#用子类申明对象s
s.check1()									#s调用父类中的函数
s.check2()									#s调用子类中的函数
print(s.fir,s.sec)								#输出s父类和本身的属性变量