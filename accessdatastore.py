
import datastore as x
import threading
import time

x.create("thani",25)
x.create("src",70,3600) 
x.read("thani")
x.read("src")
x.create("thani",50)
x.modify("thani",55)
x.delete("thani")

#using threading

t1=threading.Thread(target=(x.create),args=("thani",15,1000))
t1.start()
time.sleep(1)

