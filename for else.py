
nums = [12,3,5,2,5,6,3]

mm=([x for x in nums if x%5==0 ])
print(mm)


for num in nums:
    if num %5==12:
        print(num)
        break

else:
    print("not found")

