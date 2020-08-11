'''定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造'''
from xiaohongxing.hometown.home_002 import TongLao
class XuZhu(TongLao):
    def __init__(self, hp, power):
        super().__init__(hp, power)

    def read(self, read):
        print("罪过罪过")
a = XuZhu(300,60)
a.fight_zms(600, 90, "邹市明")
a.read("虚竹")

