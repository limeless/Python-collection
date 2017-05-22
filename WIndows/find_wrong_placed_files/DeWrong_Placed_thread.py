from glob import glob
import logging, time, os, queue, threading
import threading

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        #print ("Start Threading : " + self.name)
        process_data(self.name, self.q)
        #print ("Exiting Threading : " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            #print("[WALK] %s /"% data)
            pics = os.listdir(data)
            for pic in pics:
                if pic.endswith(".jpg"):
                    if data not in pic:
                        logging.warning('[ERRO] %s / %s' % (threadName, data, pic))
                    else:
                        print('[PASS] %s / %s' % (data, pic))
                        pass
                time.sleep(0.3)
        else:
            queueLock.release()
        time.sleep(1)

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(d)]
    
if __name__ == '__main__':
    logging.basicConfig(filename='wrong_placed.log', filemode='w', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s ')
    #find_pics()
    threadList = ["Worker1", "Worker2", "Worker3", "Worker4", "Worker5"]
    nameList = listdirs(".")
    queueLock = threading.Lock()
    workQueue = queue.Queue()
    threads = []
    threadID = 1

    # 创建新线程
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

    # 等待队列清空
    while not workQueue.empty():
        pass

    # 通知线程是时候退出
    exitFlag = 1

    # 等待所有线程完成
    for t in threads:
        t.join()
    print ("Done")
