#howv to search in a list using function
"""
def search(list,n):         #my search functio
    i = 0
    while i <len(list):
        if list[i] ==n:
            return True;
        i +=1

    return False;

list = [5,3,6,7,3,4]
n = 6

if search(list,n):
    print("found at",list.index(n))
else:
    print("not found")
    """

# def searchs(nums, n):
#     for i in len(nums): ther is a problem here
#         if nums[i] ==n:
#             return True;
#
#     return False;
#
#
# nums = [2,5,43,67,5,3]
# m= 4
#
# if searchs(nums,m):
#     print("found",nums.index(m))
# else:
#     print("not found")

def man():
    print("i am a good boy")
    man()

man()


