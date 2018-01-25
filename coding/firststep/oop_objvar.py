# coding=UTF-8

class Robot:
    """表示有一个带有名字的机器人"""
    # 一个类变量，用来技术机器人的数量
    population = 0

    def __init__(self,name):
        """初始化数据"""
        self.name = name
        print("(Initializing({}))".format(self.name))

        # 当有机器人被创建时，机器人会增加人口的数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        """来自机器人真诚的问候"""
        print('Gretting,my master call me {}.'.format(self.name))

    @classmethod
    def how_may(cls):
        """打印当前的人口数量"""
        print("we have {:d} robots.".format(cls.population))


droid1 = Robot("r2-D2")
droid1.say_hi()
Robot.how_may()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_may()

print("\nRobots con do some work here.\n")

print("Robots have finished their work,So let's destory them")
droid1.die()
droid2.die()

Robot.how_may()