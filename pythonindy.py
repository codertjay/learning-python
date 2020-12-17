
# print(12)
#
# print('hello world')
# def name(name):
#     print('hello my name is favour '+name)
#
#
# print(222)
# name('afenikhena')
#
# a = 15
# b = 12
# x = (a//4 +b **3) < 2000 and (b % 4 != 0)
# print(x)

#
# for i in range (10,3,-1):##this is to print i in descending order
#     print(i)


#
# av = 5
# x = 12
#
# i =1
# while i <= x:
#     print(i)
#     i+=1
#     if i<=av:
#         break

#
# for j in range (5):
#     for i in range (4 -j ):
#         print('#',end = "")
#     print('')
# rang = [4]

#
# #using row and column
# for k in range (2):
#     for row in rang:
#         print('ABQR\nABCR\nABCD',end='')#this end is use to prevent column
#     print('')

# array


# vals = array('l',[3,-4,2,7,2])##here i used unsigned long means i print from minus to plus in my array
# print(vals.buffer_info())
# print(vals)
#
# ##what if you want to use loops in an array
#
# for i in vals:
  #  print(i)


##this way i want to get response from a user in this array

# stud = array('i',[4,-6,7,3])
#
# stud.append(12)##adding something to the list
# print(stud)
# stud.insert(1,3)
# print(stud)
# print(stud.itemsize)##the original size of the array
# print(len(stud))##the length of the array after apppending and inserting


## inserting element in an array
#

# arr = array('i',[])
#
# n = int(input(' Enter the length of the array: '))
#
# for i in range (4):##i am using a loop to get the array number 4 times
#     x = int(input(' Enter the next of the array: '))
#     arr.append(x)##here i am adding to the arrany
#
# print(arr)
#
#
# val = int(input('Enter an index to search for a value in the array: '))
# print(arr.index(val))## here i am using functions to search index number



## there are two types of :
# two dimension and multi dimension array
"""
from array import *

###writing an array where u want to get response from the user

arr = array('i',[])##here i am creatin an empty square bracket
n = int(input('Enter the length of the array'))


for i in range(4):##so the user ask 4 trimes and i would add it in the array
    z = int(input('List of numbers you wnat to put in this array: '))
    arr.append(z)

print(arr)

a = int(input('get the index of an array just input the number'))
print(arr.index(a))
"""

class man:
    def exit(self):
        print('running  and compiling')

class woman:
    def exit(self):
        print('all of the abover mentioned')
        print('still running')

class gos:
    def exit(self):
        print(" i wont work")


class animal:
    def name(self,ide):
        ide.exit()


ide = gos()
m1 = animal()
m1.name(ide)




print(int.__add__(4,4))










