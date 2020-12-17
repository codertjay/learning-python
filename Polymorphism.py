#polymorphism is onething that works in diffenrent ways



##   Duck Typing
"""
class Pycharm:

    def execute(self):
        print("compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("convention check")
        print("compiling check")
        print("running check")
class Laptops:


    def code(self,ide): ##i am using this class to access other class
        ide.execute() ##this way i am callling the function  under this function


ide = MyEditor()
 ##so if ide is equal to MyEditor that means everything under
## my editor is stored on ide
lap1 = Laptops()
 ## i am callling the class
lap1.code(ide)
 #this is where i put the ide

"""
##   DUCK TYPING
"""
class favour:

    def man(self):
        print("i have being "
              "called")

class moses: ## i am changing the class  name
    def man(self):
        print("still running just wait for a few minute")


class david : #  i am using this one to call all the class
    def woman(self,ide):
        ide.man() ## this is whare i am calling al the function name man()
                ##so iam calling the first class finctionb and the second class function


ide = moses() # i only just change the class name it or be favour or moses
fav1 = david()
fav1.woman(ide) #so this is what gives the output
"""



##SECOND TYPE OF POLYMORPHISM
##     OPERATION OVERLOADING IN PYTHON
"""
a = 5
b = 6

print(a +b)
print(int.__mul__(a,b))
print(str.lower("FAVOUR"))


class student:

    def __init__(self,n1,n2):
        self.n1 =n1
        self.n2 = n2

    def __add__(self, other):
        n1 = self.n1 + other.n1
        n2 = self.n2 + other.n2
        return n1
        return n2
        return n1 + n2
        n3 = student(n1,n2)


m1 = student(1,3)
m2 = student(14,34)
print(m1 +m2)
"""

## this is  METHOD OVERLOADING
## THIS WAY U CAN ADD TWO NUMBERS THREE ROR AS MUCH AS YOU WANT
# USING  FUNCTION AND NONE AND THE IF STATEMENT AFTER USING THE (INITIAL) THIS
# INITIAL IS YOUR CHOICE
"""
class student:

    # def __init__(self,n1,n2):
    #     self.n1 =n1
    #     self.n2 = n2


    def sum(self,a=None,b= None,c=None,d = None):
        s = 0

        if a!=None and b!=None and c!=None and d!=None:# here is adding a +b+c+d only
            s = a + b + c +d
        elif a!=None and b!=None and c!=None:# here is adding a +b +c only
            s = a + b +c

        elif a!=None and b!=None: # here is adding a +b only
            s = a + b
        else:      # here is giving only a
            s = a

        return s

c1 = student()
print(c1.sum(1, 2,4,5)) # because i use return in the function that is why i am 
#calling it with print
"""

## METHOD OVERIDING
## this is just like inheritance
"""
class A :
    def show(self):
        print("A is in show ")

class B(A): # b have inherited everything on a just like child and father

    def show(self):
        print("has being overided")



a1 = B()
a1.show()  #this is where i am calling it
"""

