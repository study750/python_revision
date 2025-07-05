import multiprocessing
import time
def call1():
    time.sleep(2)
    

def call2():
    time.sleep(2)

p1=multiprocessing.Process(target=call1)
p2=multiprocessing.Process(target=call2)

p1.start()
p2.start()

p1.join()
p2.join()

# call1()
# call2()