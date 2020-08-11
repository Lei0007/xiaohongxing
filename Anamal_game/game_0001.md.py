'''

用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。

'''
class Persion():
    name = 'China sun'

# 构造函数定义属性
    def __init__(self, name, hometown, age, job):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.job = job
    @classmethod
    def eat(self):
        print("eating")

    def jump(self):
        print(f"{self.name} jump")

    def play(self):
        print("playing")


print(Persion.eat())

zs = Persion("zhangsan", "广州", 26, "拳击运动员")
print(zs.name)

zx = Persion('zhangsan', '上海', 36, '篮球运动员')
print(zx.job)

print(f"zhangsan 的名字为: {zx.name}, zhangsan的家乡为: {zx.hometown}, zhangsan 的年龄为: {zx.age}, zhangsan 的职业为: {zx.job}")

li = Persion('lisi', '北京', 56, '教练')

print(f"li 的名字为: {li.name}, ")






