"""
输入m和n，计算组合数C(m,n)的值

Version: 1.0
Author: 骆昊
"""

'''m = int(input('m = '))
n = int(input('n = '))
# 计算m的阶乘
fm = 1
for num in range(1, m + 1):
    fm *= num
# 计算n的阶乘
fn = 1
for num in range(1, n + 1):
    fn *= num
# 计算m-n的阶乘
fk = 1
for num in range(1, m - n + 1):
    fk *= num
# 计算C(M,N)的值
print(fm // fn // fk)'''

#try to definate hanshu
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result
print(fac(3))

'''from math import factorial
m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n)//factorial(m-n)),,,

