languages = ['Python', 'Java', 'C++', 'JavaScript']
print(languages)
languages.insert(1,'SQL')
print(languages)
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)
languages = {'python','python'}
languages.remove('python')
print(languages)#这是什么鬼
languages.clear()
items = ['Python', 'Java', 'C++']
del items[1]
print(items)


items = ['Python','Java','Java','C++','Kotlin','Python']
print(items.index('Python'))
print(items.index('Python',1))
print(items.count('Python'))

#print(items.index('Java',3))


items = ['Python','Java','C++','Kotlin','Swift']
items.sort()
print(items)
items.reverse()
print(items)

items =[]
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items = [i for i in range(1,100) if i%3 == 0 or i%5 ==0]
print(items)

nums1 =[35,12,97,64,55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)

nums1 = [35,12,97,64,55]
nums2 = [num**2 for num in nums1]
print(nums2)


nums1 = [35,12,97,64,55]
nums2 = []
for num in nums1:
    if num >50:
        nums2.append(num)
print(nums2)

nums1 = [35,12,97,64,55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

scores = [[95,83,92],[80,75,82],[92,97,90],[80,78,69],[65,66,89]]
print(scores[0])
print(scores[0][1])

'''scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score =int(input('请输入：'))
        temp.append(score)
    scores.append(temp)
print(scores)'''


import random

scores = [[random.randrange(60,101) for _ in range(3)] for _ in range(5)]
print(scores)


import random

red_balls = list(range(1,34))
select_balls = []
for _ in range(6):
    index = random.randrange(len(red_balls))
    select_balls.append(red_balls.pop(index))
select_balls.sort()
for ball in select_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end='')
blue_ball = random.randrange(1,17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')


import random

red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
select_balls = random.sample(red_balls,6)
select_balls.sort()
for ball in select_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end='')
blue_ball =random.choice(blue_balls)
print(f'\033[034m{blue_ball:0>2d}\033[0m')


import random

n = int(input('生成几注号码：'))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
for _ in range(n):
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    for ball in select_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end='')#0>2d是什么鬼
    blue_ball = random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')


import random

from rich.console import Console
from rich.table import Table


console = Console()

n = int(input('生成几注号码：'))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
table = Table(show_header=True)
for col_name in('序号','红球','蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    blue_ball = random.choice(blue_balls)
    table.add_row(
        str(i+1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in select_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )
console.print(table)