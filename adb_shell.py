import time
import subprocess
from PIL import Image
import random

poweron = 'adb shell input keyevent 26'
up_swipe = 'adb shell input swipe 550 1750 550 1250 500'
home = 'adb shell input keyevent 3'
clear_menu = 'adb shell input keyevent 82'
clear_right = 'adb shell input tap 550 1700'
hit_app = 'adb shell input tap 400 1750'
back = 'adb shell input keyevent 4'
long_bsck = 'adb shell input keyevent --longpress 4'


def get_picture():
          a = subprocess.Popen('adb shell screencap -p',shell = True, stdout = subprocess.PIPE)#screencap -p
          a = a.stdout.read()
          a = a.replace(b'\r\r\n',b'\n')
          times = time.strftime('%m-%d~%H：%M：%S')
          print('get picture', times)
          with open ('%s.png'% times,'wb') as f:
                    f.write(a)
def doit(strs_shell):
          a = subprocess.Popen(strs_shell,shell = True, stdout = subprocess.PIPE)#screencap -p
          a = a.stdout.read()
          a = a.replace(b'\r\r\n',b'\n')
          print(strs_shell, a)
          time.sleep(2)

def morning():
          print ('this is morning')
          doit(poweron)
          doit(up_swipe)
          doit(home)
          doit(clear_menu)
          doit(clear_right)
          doit(hit_app)
          time.sleep(8)
          get_picture()
          doit(home)
          doit(clear_menu)
          doit(clear_right)
          doit(poweron)
          print('morning is over')
          pass

def afternoon():
          print ('this is afternoon')
          # b步骤
          print('afternoon is over')
          pass
          
def runtime():
          while True:
                    random_number = random.randrange(0,10,1)
                    random_AM_time = '08:3%s' % random_number
                    random_PM_time = '18:1%s' % random_number
                    while True:
                              now_week = time.strftime('%w')
                              now_time = time.strftime('%H:%M')
                              print('get_random_time\nAM = ',random_AM_time,'  PM = ',random_PM_time,'   Now_week = ',now_week, '  Now_time = ', now_time)
                              # print(type(random_AM_time), type(now_time))
                              if random_AM_time == now_time:
                                        morning()
                                        time.sleep(2)
                                        break
                              if random_PM_time == now_time:
                                        afternoon()
                                        time.sleep(2)
                                        break
                              time.sleep(29)

#morning()
runtime()                              


