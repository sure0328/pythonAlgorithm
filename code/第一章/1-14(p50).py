class Fruit:								#定义类
    total = 0
    def __init__(self,FruitN,prize,number):
        self.name = FruitN
        self.number = number
        self.prize = prize
        Fruit.total += prize*number

	def FruitData(self):
        print(self.name,self.number,self.prize)

fruit1 = Fruit('Melon',10,2)						#申明对象1
fruit2 = Fruit('Apple',2,5)						#申明对象2
fruit3 = Fruit('Cherry',1,15)						#申明对象3
fruit1.FruitData()							#调用函数
fruit2.FruitData()
fruit3.FruitData()
print(Fruit.total)								#调用类的属性