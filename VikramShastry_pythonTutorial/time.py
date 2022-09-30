from datetime import datetime

currSec = datetime.today().second 
odds = [1,3,5,7,9]
if currSec in odds:
    print('this is an odd moment')
    print('hoo haaa')
else:
    print('this is not so odd at all')    
    print('done')
print('realy.done')