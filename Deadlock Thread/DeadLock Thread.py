from threading import *

l1=Lock()
l2=Lock()

def bookticket():
	l1.acquire()
	print("Book ticket locked train")
	print("Bookticket wants to lock on compartment")
	l2.acquire()
	print("Bookticket locked compartment")
	l2.release()
	l1.release()
	print("Booking ticket done...")
	
def cancelticket():
	l2.acquire()
	print("Cancel ticket locked train")
	print("Cancelticket wants to lock on compartment")
	l1.acquire()
	print("Cancelticket locked compartment")
	l1.release()
	l2.release()
	print("Cancellation of ticket is done...")
	
t1=Thread(target=bookticket)
t2=Thread(target=cancelticket)
t1.start()
t2.start()
