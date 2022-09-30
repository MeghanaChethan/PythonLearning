from datetime import datetime
import random
import time 

odds =[1,2,3,4,5,6, 45, 452,67,8,23,56]

times = 5

print('odds = '+str(odds))
for  x in range(0,times):
    pauseSecs = random.randint(0,4)
    time.sleep(pauseSecs)
    currSec = datetime.today().second
    print('currSec = '+str(currSec))
    if currSec in odds:
            print('this is an odd moment '+str(x))
    else:
            print('this is not an odd moment '+str(x))

print('done')