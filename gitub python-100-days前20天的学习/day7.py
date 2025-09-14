'''for num in range(1,101):
    end = int(num**0.5)
    is_prime = True
    for i in range(2,end+1):
        if num%i==0:
            is_prime = False
            break
    if is_prime:
        print(num)'''

'''a,b = 0,1
for _ in range(0,20):
    a,b = b,a+b
    print(a)'''

'''for num in range(100,1000):
    low=num%10
    mid=num//10%10
    high=num//10//10
    if num==low**3+mid**3+high**3:
        print(num)'''


'''for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')'''


'''for x in range(0, 21):
    for y in range(0, 34):
        z=100-x-y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')'''



import random

money = 1000
while money > 0:
    print(f'你的资金为{money}')
    while True:
        debt = int(input('debt = '))
        if 0 < debt <= money:
            break
    first_point = random.randint(1,7) + random.randint(1,7)
    print(f'\n玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print(f'玩家胜\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print(f'庄家胜\n')
        money -= debt
    else:
        while True:
            current_point = random.randint(1,7) + random.randint(1,7)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print(f'庄家胜\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜\n')
                money += debt
                break
print('你破产了\n')