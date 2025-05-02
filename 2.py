from threading import Thread
from time import sleep
from random import randint
import os

def DTOB(x):
    x=x
    b=""
    while x != 0:
        b = str((x % 2)) + b
        x = x // 2
    return b

x = randint(0,100)
#stop_event = Event()
print(DTOB(x))
class c1(Thread):
    def run(self):
        sleep(10)
        #if not stop_event.is_set():
        print(f"\nTime is up! The answer was {x}")
        os._exit(0)
        #I need the code to stop c2 here
class c2(Thread):
    def run(self):
        try:
            u_inp = int(input("Enter the number: "))
            #if stop_event.is_set():
            #    return
            if u_inp == x:
                print("Correct!")
            #    stop_event.set()  # Stop timer
                os._exit(0)
            else:
                print(f"Wrong. The answer was {x}")
            #    stop_event.set()
                os._exit(0)

        except ValueError:
            print("Invalid input.")
        #stop_event.set()


t1 = c1() # create class 1
t2 = c2() # create class 2

t1.start() # start class 1
t2.start() # start class 2

#wait for both classes to finish to avoid exiting the thread program early
t1.join()
t2.join()
