class Fruit:								#定义类
    total = 0
    def __init__(self,FruitN,prize,number):
        self.name = FruitN
        self.number = number
        self.prize = prize
        Fruit.total += prize*number

	def FruitData(self):
        print(self.name,self.number,self.prize)

f = Fruit()								#申明对象
f.test1 = 123							#添加属性test1
f.test1 = 134							#更改属性test1的值
del f.test1								#删除属性test1