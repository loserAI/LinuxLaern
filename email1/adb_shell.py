import time
import subprocess
from PIL import Image


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
          return times
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
          a = get_picture()
          doit(home)
          doit(clear_menu)
          doit(clear_right)
          doit(poweron)
          print('morning is over')
          return a
          

def afternoon():
          print ('this is afternoon')
          # b步骤
          doit(poweron)
          doit(up_swipe)
          doit(home)
          doit(clear_menu)
          doit(clear_right)
          doit(hit_app)
          time.sleep(8)
          doit()
          print('afternoon is over')
          pass
                          
if __name__ == '__main__':
          print('________________________以下是测试____________')
          morning()

