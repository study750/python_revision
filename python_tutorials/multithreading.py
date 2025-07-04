import time
import threading
def call1(msg):
    i=0
    while(i<5):
        time.sleep(0.2)
        print(msg)
        i+=1

def call2(msg):
    i=0
    while(i<5):
        time.sleep(0.2)
        print(msg)
        i+=1



start = time .time()
msg1="hi"
msg2="bhus"
thread1= threading.Thread(target=call1,args=(msg1,))
thread2= threading.Thread(target=call2,args=(msg2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end=time.time()

print(int(end-start)*1000)