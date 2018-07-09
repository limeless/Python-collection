import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from fake_useragent import UserAgent
import re
import time, os, queue, threading, chardet

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        #print ("開始線程 : " + self.name)
        process_data(self.name, self.q)
        #print ("結束線程 : " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            temp_list = q.get()
            queueLock.release()
            url = temp_list[0]
            title = temp_list[1]
            useragent = temp_list[2]
            if 'Re:' in title:
                title = title.replace('Re: ', 'Re_')
                print('文章標題處理: {}'.format(title))
            elif 'Fw:' in title:
                title = title.replace('Fw: ', 'Fw_')
                print('文章標題處理: {}'.format(title))
            res = requests.get(url, headers=useragent)
            soup = BeautifulSoup(res.text, 'lxml')
            if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
                print('{}: 正在尋找正妹……'.format(threadName))
                for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
                    try:
                        urlretrieve(img_url['href'], 'D:\Beauty\{}_{}.jpg'.format(title, index))
                        print('{}: {} {}_{}.jpg 下載成功!'.format(threadName, img_url['href'], title, index))
                    except:
                        print('{}: {} {}_{}.jpg 下載失敗!'.format(threadName, img_url['href'], title, index))
                    
                    time.sleep(0.1)
        else:
            queueLock.release()
        #time.sleep(1)
if __name__ == '__main__':
    pagenum = 1200
    print('讀取 User Agent 中...')
    ua = UserAgent()
    while pagenum < 2559:
        exitFlag = 0
        #threadList = ["大叔甲", "大叔乙", "大叔丙", "大叔丁", "大叔戊"]
        threadList = []
        for x in range(1,10):
            threadList.append(x)
        queueLock = threading.Lock()
        workQueue = queue.Queue()
        threads = []
        threadID = 1

        for tName in threadList:
            thread = myThread(threadID, tName, workQueue)
            thread.start()
            threads.append(thread)
            threadID += 1
        
        queueLock.acquire()
        print('目前頁面: {}'.format(pagenum))
        curres = 'https://www.ptt.cc/bbs/Beauty/index{}.html'.format(pagenum)
        useragent = {'User-Agent': ua.random}
        print('偽裝為裝置: {}'.format(useragent))
        res = requests.get(curres, headers=useragent)
        soup = BeautifulSoup(res.text, 'lxml')
        print('正在爬取頁面: {}'.format(curres))
        for article in soup.select('.r-ent a'):
            temp_list = []
            url = 'https://www.ptt.cc' + article['href']
            title = article.text
            if 'search' in url:
                pass
            elif '[帥哥]' in title:
                print('發現非正妹, 跳過！ {}'.format(title))
                pass
            elif '鲜肉' in title:
                print('發現非正妹, 跳過！ {}'.format(title))
                pass
            elif '男' in title:
                print('發現非正妹, 跳過！ {}'.format(title))
                pass
            else:
                temp_list.append(url)
                temp_list.append(title)
                temp_list.append(useragent)
                workQueue.put(temp_list)
        queueLock.release()

        while not workQueue.empty():
            pass
        
        exitFlag = 1
        
        for t in threads:
            t.join()
        print ("完成頁面: {}".format(curres))
        pagenum += 1
        time.sleep(2.0)
    print('全部完成')
