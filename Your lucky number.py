from random import seed
from random import random

def lucky_number(name):
    number =round(len(name) * random())
    print("Hello " + name + " your lucky number is " + str(number))

lucky_number("Carlos")