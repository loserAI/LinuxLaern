import time
import random
import adb_shell
import email_simple



while True:
        random_number = random.randrange(0,10,1)
        random_AM_time = '08:3%s' % random_number
        random_PM_time = '18:1%s' % random_number
        print('get_random_time\nAM = ',random_AM_time,'  PM = ',random_PM_time)
        while True:
                now_week = time.strftime('%w')
                # print(type(now_week))
                now_time = time.strftime('%H:%M')
                random_AM_time = now_time
                print('random_time\nAM = ',random_AM_time,'  PM = ',random_PM_time,'   Now_week = ',now_week, '  Now_time = ', now_time)
                # print(type(random_AM_time), type(now_time))
                if now_week in "123456":
                        if random_AM_time == now_time:
                                  print('runing.....')
                                  name = adb_shell.morning()
                                  print(name)
                                  email_simple.sendemail(name,'完成打卡')
                                  print('sleep(10000)')
                                  time.sleep(10000)
                                  break
                        if random_PM_time == now_time:
                                  adb_afternoon.afternoon()
                                  print(name)
                                  email_simple.sendemail(name,'完成打卡')
                                  print('sleep(10000)')
                                  time.sleep(10000)
                                  break
                        time.sleep(29)
		
                else :
                        print('sleep 86400')
                        time.sleep(86400)
                        email_simple.sendemail('wife','this is your wife')
