#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ll = str(number)
lastd = ll[-1:]
if int(lastd) == 0:
    print("Last digit of {} is {} and is 0".format(number, int(lastd)))
elif number < 0:
    print("Last digit of {} is -{} and is less than 6 and not 0"
          .format(number, int(lastd)))
else:
    print("Last digit of {} is {} and is ".format(number, int(lastd)), end='')
    if int(lastd) > 5:
        print('8greater than 5')
    else:
        print('less than 6 and not 0')
