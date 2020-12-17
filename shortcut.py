
#this way i am using normal function and creating nedw list and squaring the liust


#my functio for squaring a list and creating anotherf list
"""
def esp(list1):
    list2 = []
    for x in list1:
        list2.append(x **2)
    print(list2)

list= [2,45,45,4,23,5]
esp(list)
"""

#but there is another way i can do it i would just use gthe map cfunction and lambdac function
#the map function is justr like a loop function


lis= (2,3,4,5,6)
n = 2

        #short form of sqauring a list
print([x**2 for x in lis])
        #just printing a list
print([x for x in lis])
        #using an if statement in a list
print([m for m in lis if m <4])

        #getting the even number in a list
print([m for m in lis if m%2==0])

m=(x for x in range(10))
print(m.__next__())#this way i am printing the next value from i12 to ten
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())




##   YEILD
#yield is a special function which is just like  return but the differnce between
#yield and return is that return terminate the function but yield still continues the statement



def topten(n):
    i=0
    while i<n:
        i=i*i
        yield i
        i+=1

for x in topten(2):
    print(x)



















