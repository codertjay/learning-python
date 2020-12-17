# this enable you to print a lot of codecby adding classes
from time import sleep
from threading import  *
"""
class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start()
t2.start()
"""
from colorama import Fore,init
class human(Thread):
    def run(self):
        for i in range(10):
            age=input("How old are you")
            print(age)
            sleep(1)
class animal(Thread):
    def run(self):
        for i in range(10):
            name = input("what is your name ")
            print(Fore.RED +name + "💖💖💖")
            sleep(1)



m1= animal()
m2 = human()
m1.start()
sleep(0.2)
m2.start()






