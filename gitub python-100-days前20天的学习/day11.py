s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)
#\r 回车符怎么用还有\t制表符怎么用

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'#还可以表示中文！
print(s1)
print(s2)

s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)

s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!

s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))            # 39558
print(ord('昊'))            # 26122
s4 = '王大锤'
print(ord('王'))            # 29579
print(ord('大'))            # 22823
print(ord('锤'))            # 38180
print(s3 >= s4)             # True
print(s3 != s4)             # True

s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba

s = 'hello'
for i in range(len(s)):
    print(s[i])

s = 'hello'
for elem in s:
    print(elem)


s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE

s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
#print(s.index('or', 9))  # ValueError: substring not found

s = 'hello world!'
print(s.find('o'))       # 4
print(s.rfind('o'))      # 7
print(s.rindex('o'))     # 7
# print(s.rindex('o', 8))  # ValueError: substring not found

s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s2.isalnum())  # True

s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033

a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))

a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))

a = 321
b = 123
print(f'{a} * {b} = {a * b}')

"""变量值	占位符	格式化结果	说明
   3.1415926	{:.2f}	'3.14'	保留小数点后两位
   3.1415926	{:+.2f}	'+3.14'	带符号保留小数点后两位
  -1{:+.2f}	'-1.00'	带符号保留小数点后两位
   3.1415926	{:.0f}	'3'	不带小数
   123	{:0>10d}	'0000000123'	左边补0，补够10位
   123	{:x<10d}	'123xxxxxxx'	右边补x ，补够10位
   123	{:>10d}	'       123'	左边补空格，补够10位
   123	{:<10d}	'123       '	右边补空格，补够10位
   .123	{:.2%}	'12.30%'	百分比格式
    123456789	{:.2e}	'1.23e+08'	科学计数法格式"""

