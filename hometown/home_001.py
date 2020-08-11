'''

用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。

'''
class Anamal:
    print("动物类")
    def __init__(self,eat, drink, dump, sleep):
        self.eat = eat
        self.drink = drink
        self.dump = dump
        self.sleep = sleep
    def eat(self):
        print("eating")
    def fight(self):
        print("会厮杀")

class Persion:
    print("人类")
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
    def quanji(self):
        print("会打拳击比赛")
        print("打地下黑拳谋生")
    def swim(self):
        print("会游泳")

class game_Hero:
    print("游戏人物")
    def __init__(self, Hp, power, fashu):
        self.Hp = Hp
        self.power = power
        self.fashu = fashu
    def feixiang(self):
        print("会飞翔")

class PersinoHero:
    print("人民英雄")
    def __init__(self, name, age, deed):
        self.name = name
        self.age = age
        self.deed = deed
    def hometown(self):

        print("家乡")

zs = Anamal('吃','喝', '站', '睡觉')
zs.fight()
print(f"zs会: {zs.eat}, zs会: {zs.drink}, zs会: {zs.dump}, zs会: {zs.sleep}")

li = Persion('lii', 30, '模特')
print(f"lii的名字为: {li.name}, lii的年纪为: {li.age}, lii的职业为: {li.job}")
li.swim()
li.quanji()

zhaoliu = PersinoHero('zhaoliu', 84, '抗击疫情')
print(f"钟南山名字为: {zhaoliu.name},钟南山的年纪为:{zhaoliu.age},钟南山事迹为: {zhaoliu.deed}")
zhaoliu.hometown()

wangwu = game_Hero(1000, 60, '法术')
wangwu.feixiang()



