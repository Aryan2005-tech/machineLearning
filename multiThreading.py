import threading
import time
def numbers():
    for i in range(5):
        print(f"number - {i}\n")
        time.sleep(1)
def letters():
    for i in "abcde":
        print(f"letter - {i}\n")
        time.sleep(1)
t1=threading.Thread(target=numbers)  
t2=threading.Thread(target=letters)
t=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
finished=time.time()-t
print(finished)              
