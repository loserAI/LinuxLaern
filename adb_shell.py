import time
import subprocess
from PIL import Image
import random

poweron = 'adb shell input keyevent '

def git_picture():
          a = subprocess.Popen('adb shell screencap -p',shell = True, stdout = subprocess.PIPE)#screencap -p
          a = a.stdout.read()
          a = a.replace(b'\r\r\n',b'\n')
          with open ('test.png','wb') as f:
                    f.write(a)
def doit(strs_shell):
          a = subprocess.Popen(strs_shell,shell = True, stdout = subprocess.PIPE)#screencap -p
          a = a.stdout.read()
          a = a.replace(b'\r\r\n',b'\n')
          print(a)
          time.sleep(2)
          
def runtime():
          while True:
                    random_number = random.randrange(0,10,1)
                    random_AM_time = '08:3%s' % random_number
                    print('get_random_time = ',random_AM_time)         
                    while True:
                              print('sleep 2')
                              if True:
                                        time.sleep(2)
                                        break
                              if 1:
                                        break
runtime()                              
git_picture()

