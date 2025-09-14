"""height=float(input('身高(cm):'))
weight=float(input('体重(mg)'))
bmi=weight/(height/100)**2
print(f'{bmi=:.1f}')"""
'''if 18.5 <= bmi < 24:
    print('你的身材很棒')'''
'''else:
    print('你的身材不够标准哦！')'''
'''if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 25:
    print('你的身材很棒!')
elif bmi < 30:
    print('你的体重过重！')
elif bmi < 35:
    print('你已中度肥胖!')
else:
    print('你已过度肥胖！')'''
'''status_code=int(input('响应状态码：'))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
print('状态码描述：', description)'''
'''x = float(input('x:'))
if x > 1:
    y = 3*x-5
elif x >= -1:
    y = x + 2
else:
    y = x + 1
print(f'{y=}')'''

'''score=float(input('score:'))
if score >=90:
    grade='A'
elif score >=80:
    grade='B'
elif score >=70:
    grade='C'
elif score >=60:
    grade='D'
else:
    grade='E'
print(f'{grade = }')'''

a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
if a+b>c and a+c>b and b+c>a:
    perimeter=a+b+c
    s=perimeter/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print(f'面积；{area}')
else:
    print('不能构成三角形')