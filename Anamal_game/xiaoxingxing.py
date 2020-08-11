'''import turtle
import time
turtle.speed("fastest")
turtle.pensize(1)
for y in range(100):
    turtle.forward(3 * y)
    turtle.left(20)
    turtle.right(175)
'''

class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        self.name = name
        if name == "wyz":
            print("师弟！！！")
        elif name == "李秋水":
            print("配件人")
        elif name == "丁春秋":
            print("叛徒")
        else:
            print(f"姓名{self.name}")
        def fight_zms(self, enemy_name, enemy_hp, enemy_power):
            self.enemy_name = enemy_name
            self.enemy_hp = enemy_hp
            self.enemy_power = enemy_power
            power = self.power*10
            while True:
                self.hp = self.hp -self.enemy_power
                self.enemy_hp = self.enemy_hp - self.power
                if self.hp > self.enemy_hp:
                    print(f"{self.name}赢了")
                    break
                elif self.hp < self.enemy_hp:
                    print(f"{self.enemy_name赢了}")
                    break
wyz = TongLao(1000,60)
wyz.see_people("丁春秋")
wyz.fight_zms("张三", 100, 9)