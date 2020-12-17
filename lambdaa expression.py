# we use lambda function to create a short function thatv gives only one output

a = lambda x,y,a:(x**2) +(y*2) +(a)
print(a(2,3,4))

m = lambda x=input("what is your name:"),y=input("how old are you"): f"my name is {x} and i am  {y} years old"

print(m())

n = lambda x,y: x if x>y else y

print(n(12,34))

w = lambda x,q:(x**q)
print(w(2,4))
