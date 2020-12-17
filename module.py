# for i in range(6 ):
#     for x in range(4):
#         print('#',end=' ')
#     print()

from array import *

# stud = array('i',[4,-6,7,3])
#
# stud.append(12)##adding something to the list
# print(stud)
# stud.insert(1,3)
# print(stud)
# print(stud.itemsize)##the original size of the array
# print(len(stud))##the length of the array after apppending and inserting



ss = array('b',[1,32,34,4])
mm = array(ss.typecode,(a for a in ss))

print(type(mm))




def gets():
    print("hello")
    gets()

gets()



