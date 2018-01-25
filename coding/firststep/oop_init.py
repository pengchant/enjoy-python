class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Hello,my name is ',self.name)

p = Person('chenpeng')
p.say_hi()
# 同样的也可以这样写Person('Swaroop').say_hi()

