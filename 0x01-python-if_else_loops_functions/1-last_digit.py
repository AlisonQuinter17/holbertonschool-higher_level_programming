#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ll = str(number)
lastd = ll[-1:]
if int(lastd) == 0:
    print("Last digit of {} is {} and is 0".format(number, lastd))
elif number < 0:
    print("Last digit of {} is -{} and is ".format(number, lastd), end='')
    print('less than 6 and not 0')
else:
    print("Last digit of {} is {} and is ".format(number, lastd), end='')
    if int(lastd) > 5:
        print('greater than 5')
    elif int(lastd) == 0:
        print('0')
    else:
        print('less than 6 and not 0')
