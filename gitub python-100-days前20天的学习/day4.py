print(100%9)
print(100//13)
print(321**12)

print((2+3*8)**2)
print(((2+3)*8)**2)

a=10
b=3
a+=b
a*=a+2
print(a)
print(13*15)

#print(a=10)
#TypeError: print() got an unexpected keyword argument 'a'
#prit((a=10))
#SyntaxError: invalid syntax.
print((a:=10))

'''f=float(input("请输入华氏温度："))
c=(f-32)/1.8
print('%.1f华氏温度=%.1f摄氏温度'%(f,c))

f=float(input("请输入华氏温度："))
c=(f-32)/1.8
print(f'{f:.1f}华氏温度={c:.1f}摄氏温度')'''

'''import math
radius=float(input("请输入圆的半径："))
perimeter=2*math.pi*radius
area=math.pi*radius
print('%.2f周长'%perimeter)
print('%.2f面积'%area)
print(f'周长：{perimeter:.2f}')
print(f'面积{area:.2f}')
print(f'{perimeter=:.2f}')
print(f'{area=:.2f}')'''

'''year=int(input('请输入年份：'))
is_leap=year%4==0 and year%100!=0 or year%400==0
print(f'{is_leap=}')'''