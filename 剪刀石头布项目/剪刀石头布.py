import random
from typing import overload

print('1:剪刀 2：石头 3：布,8:退出')
over = False
while not over:
    Choice = int(input('请选择：'))
    if Choice == 8:
        over = True
    while Choice <=3 and Choice>=1:
        Alchoice = random.randint(1,4)
        if Alchoice == 1:
            print('电脑出了剪刀')
        elif Alchoice == 2:
            print('电脑出了石头')
        elif Alchoice == 3:
            print('电脑出了布')
        if Choice == 1 and Alchoice == 2:
            print('电脑赢')
            print('1:剪刀 2：石头 3：布,8:退出')
            break
        elif Choice == 1 and Alchoice == 3:
            print('玩家赢')
            print('1:剪刀 2：石头 3：布,8:退出')
            i = int(input('请选择：'))
            break
        elif Choice == 2 and Alchoice == 3:
            print('电脑赢')
            print('1:剪刀 2：石头 3：布,8:退出')
            break
        elif Choice == 2 and Alchoice == 1:
            print('玩家赢')
            print('1:剪刀 2：石头 3：布,8:退出')
            break
        elif Choice == 3 and Alchoice == 1:
            print('电脑赢')
            print('1:剪刀 2：石头 3：布,8:退出')
            break
        elif Choice == 3 and Alchoice == 2:
            print('玩家赢')
            print('1:剪刀 2：石头 3：布,8:退出')
            break

        elif Choice == Alchoice:
            print('平局')
            print('1:剪刀 2：石头 3：布,8:退出')
            break