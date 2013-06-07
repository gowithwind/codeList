'''
    a function for batch task
    2013.6.7
'''
import threading
from threading import Thread
from Queue import Queue
from time import sleep

def batch(n,func,data,timeout=1):
    jobs=Queue()
    def work():
        while True:
            try:
                func,args=jobs.get(timeout = timeout)
                func(args)
                jobs.task_done()
            except:
                print 'size:',jobs.qsize()
    for i in range(n):#10 thread
        t = Thread(target=work)
        t.setDaemon(True)
        t.start()
    for i in data:
        jobs.put((func,i))
    jobs.join()
if __name__=='__main__':
    def run(task):
        print task+1    
    batch(100,run,range(0,1000))


        