# oop
#classes enable us to gather dat and function in orther for it to be use later in the future

"""
class favour:

    def __init__(self,first,last,email):
        self.first = first
        self.last = last
        self.email = first ,last, '@gmail.com'

    def man(self,first,last):
        return f"{first +last} is my fullname"


m1 = favour("thankgod","david",None)
print(m1.man('favour','dav'))
"""

#  create a class and an inheritance and use superto call the parent class
#inital in the child class

"""

class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last

        self.pay = pay

    def email(self,first,last):
        return self.first +'' +self.last+'@gmail.com'


    def fullname(self):
        return self.first +self.last

    def pay(self):
        return self.pay
    @classmethod  ## this is a class method it is not taking sef in this method
    ##and before using a method i use @classmethod
    #class method are
    #class nn:
    #age=10 so the age is not in initial so if i am using a class method this is how i
    #use it and color
    def man(cls,age,color):
        cls.age = age
        cls.color = color
        return f'{age}+{color}'


asd= Employee
print(asd.man(2,"balck"))




class manager(Employee):
     def __init__(self,first,last,pay,prog_lang):#i created my own initial by adding
         #to the employee initial

        super().__init__(first,last,pay)##i ma calling the first initial
        self.prog_lang = prog_lang



# q1 = Employee("favour","afenikhena",50000)
# print(q1.email("favour","add"))
aa = manager("fass","sdsd",2323,"java")#where i use inheritance
#i inherited everything from employee
print(aa.email('dad','sd'))#this is to get gthe email address

"""




##Magic methods
#they are those methods that are having __anything__ this is how they look like
#
mm= 'dadsd','ssdss','ss'
print(mm.__repr__())

#working with dunder method
#dunder method enable you to add object without stress you just create one
#like the dunder i use below
"""
class man:
    def __init__(self,age,color,pay):
        self.age = age
        self.color = color
        self.pay = pay
    
    def __add__(self, other):#dunder method for add
        return self.pay + other.pay

    def __len__(self):#dunder method for length
        return len(self.color)


    def __abs__(self):
        return self.pay

m1 = man(12,"dark",-500)
m2 = man(12,"light",234)
print(m1)

print(m1 + m2)#because of dunder add i was able to add pay in this way

print(m1.pay +m2.pay)#this is how i add with out the dunder method

print(len(m1))# iam calling thec length of color  without inputing m1.color
#because i have created a len function on my class
"""


# property decorators,getter setters,and deleters


class Employee:
    pass

















