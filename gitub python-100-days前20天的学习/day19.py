from tkinter.font import names


class Student:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu=Student('王大锤',20)
stu.study('Python程序设计')
#print(stu.__name)
#AttributeError: 'Student' object has no attribute '__name'

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age =age


stu =Student('王大锤',20)
stu.sex ='男'
print(stu.sex)


'''class Student:
    __slots__ = ('name','age')

    def __init__(self,name,age):
        self.name = name
        self.age =age


stu =Student('王大锤',20)
stu.sex ='男'
print(stu.sex)
AttributeError: 'Student' object has no attribute 'sex' and no __dict__ for setting new attributes'''


class Triangle(object):



    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and b + c > a and c + a > b
    #@classmethod
    #def is_valid(cls,a,b,c):
    #   """判断三条边长能否构成三角形(类方法)"""
    #   return a+ b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        return self.a + self.b + self.c


    #@property
    def area(self):
        p =self.perimeter#()
        return (p * (p - self.a) * (p -self.b) * (p - self.c)) ** 0.5

t = Triangle(3,4,5)
print(t.perimeter)
print(t.area())


class Person:


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭')


    def sleep(self):
        print(f'{self.name}正在睡觉')

class Student(Person):



    def __init__(self,name,age):
        super().__init__(name,age)

    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):



    def __init__(self,name,age,title):
        super().__init__(name,age)
        self.title = title

    def teach(self, course__name):
        print(f'{self.name}{self.title}正在讲授{course__name}.')


stu1 = Student('白元芳',21)
stu2 = Student('狄仁杰',22)
tea1 = Teacher('武则天',35,'副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')