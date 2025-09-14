'''import time
for _ in range(3600):
    print('hello world')
    time.sleep(1)'''
from operator import truediv

total = 0
for i in range(1,101,):
    if i % 2 == 0:
        total += i
print(total)

print(sum(range(2,101,2)))

total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

total = 0
for i in range(1,101):
    if i % 2 != 0:
            continue
    total += i
print(total)

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()

'''num = int(input('请输入一个正整数:'))
end = int(num**0.5)
is_peime=True
for i in range(1,end+1):
    if num % i == 0:
        is_peime=False
        break
if is_peime:
    print(f'{num}is peime')
else:
    print(f'{num} is not peime')'''

'''x = int(input('x = '))
y = int(input('y = '))
for i in range(x,0,-1):
    if x % i == 0 and y % i == 0:
        print(f'最大公约数为：{i}')
        break'''

'''x = int(input('x = '))
y = int(input('y = '))
while y % x !=0:
    x,y=y % x,x
print(f'最大公约数为：{x}')'''
#这里好像假定x<y，不是,是我搞错了

import random

answer = random.randrange(1,101)
counter = 0
while True:
    counter += 1
    num = int(input('number = '))
    if num > answer:
        print(f'bigger')
    elif num < answer:
        print(f'smaller')
    else:
        break
print(f'你一共猜了{counter}次')
