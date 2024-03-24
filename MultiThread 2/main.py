from threading import *
from time import *
class Railway:
    def __init__(self,available):
        self.available=available

    def reserve(self,wanted):
        print("Available no. of berths = ",self.available)

        if(self.available>=wanted):
            name=current_thread().name
            print('%d berths allotted for %s' %(wanted,name))
            sleep(1.5)
            self.available-=wanted
        else:
            print('Sorry, no berths to allot')
obj=Railway(1)
t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))
t1.name='First Person'
t2.name='Second Person'
t1.start()
t2.start()