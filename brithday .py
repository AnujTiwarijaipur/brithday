# happy brithday in python code 

import time
from random import randint
a=input("enter name you want wish birthday----")

for i in range(1,85):
    print('')

space = ''

for i in range(1,100):
    count = randint(1, 100)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + 'ðHappy Birthday!a',a )
    elif(i%9 == 0):
        print(space + "ð Happy Brithday ",a ) 
    elif(i%5==0):
        print(space +"ð")
    elif(i%8==0):
        print(space + "ð this year  breing happyines in Life")
    elif(i%7==0):
        print(space + "ð«")
    elif(i%6==0):
        print(space + "Happy Birthday!ð")
    else:
        print(space + "ð¸")
    space = ''
    time.sleep(0.2)




