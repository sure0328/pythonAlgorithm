class First:
 		fir = 111
 		def __init__(self):
  	   	print("Uses the first function.")
	def check1(self):
     		print("Method of the first function.")

class Second(First):
 		sec = 222
   	def __init__(self):
       	print("Uses the second function.")
   	def check1(self):						#父类方法重写
       	print("New")
   	def check2(self):
       	print("Method of the second function.")

f = First()
s = Second()
s.check1()
s.check2()
print(s.fir,s.sec)