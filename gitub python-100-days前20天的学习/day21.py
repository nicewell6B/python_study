file = None
try:
    file = open('百万富翁快车道 (【美】MJ·德马科) (Z-Library).txt','r')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定文件！')
except LookupError:
    print('指定了未知的编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
finally:
    if file:
        file.close()

class InputError(ValueError):
    pass


'''def fac (num):
    if num < 0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0,1):
        return 1
    return num * fac(num - 1)#这里不是重新定义fac函数了吗为什么还可以用这个函数

flag = True
while flag:
    num = int (input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)

try:
    with open('百万富翁快车道 (【美】MJ·德马科) (Z-Library).txt','r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开文件！')
except LookupError:
    print('指定了未知的编码')
except UnicodeDecodeError:
    print('读取文件时解码错误！')#假如不释放文件会怎么样？


try:
    with open('guido.jpg', 'rb') as file1:
        data = file1.read()
    with open('guido.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
except IndentationError:
    print('<UNK>.')'''


'''try:
    with open('百万富翁快车道 (【美】MJ·德马科) (Z-Library).txt','r',encoding='utf-8') as file1:
        data = file1.read(512)
        while data:
            file'''


'''from pathlib import Path

path = Path('百万富翁快车道 (【美】MJ·德马科) (Z-Library).txt')
contents = path.read_text('utf-8').rstrip()

print(contents)'''