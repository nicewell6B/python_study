import random



f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(2000):
    face = random.randint(1,7)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f'f1={f1}')
print(f'f2={f2}')
print(f'f3={f3}')
print(f'f4={f4}')
print(f'f5={f5}')
print(f'f6={f6}')

iteams1 = [35,12,99,68]
print(iteams1)
print(type(iteams1))
iteams2 = list(range(1,10))
iteams3 = list('hello')
print(iteams2)
print(iteams3)
print(iteams2 + iteams3)
print(iteams1 * 3)
print(2 in iteams1)
print(35 in iteams1)
print(2 not in iteams1)
iteams4 = ['apple','waxberry','durian','peach','watermelon']
print(iteams4[0])
print(iteams4[-5])
iteams4[4] = 'cow'
print(iteams4[0:4:2])
print(iteams4[0:5:2])
print(iteams4[-2:-6:-1])
iteams4[1:3] = ['x','o']
print(iteams4)


nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False
#比大小比的不是和，那怎么比？讲解漏字了，没看懂
#比的好像是第一个数字大小
languages = ['Python','Java','c++','kotlin']
for index in range(len(languages)):
    print(languages[index])#讲解漏字太严重，影响学习，我没看懂原理
#现在我看懂了，不漏字了，len其实就是计算字符个数


languages = ['Python','Java','c++','kotlin']
for language in languages:
    print(language)

import random

counters = [0]*6
for _ in range(6000):
    face = random.randrange(1,7)
    counters[face - 1] += 1
for face in range(1,7):
    print(f'{face}点出现了{counters[face-1]}次')

