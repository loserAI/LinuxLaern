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
		  print(tepy(now_week))
		  now_time = time.strftime('%H:%M')
		  print('random_time\nAM = ',random_AM_time,'  PM = ',random_PM_time,'   Now_week = ',now_week, '  Now_time = ', now_time)
		  # print(type(random_AM_time), type(now_time))
		  if now_week in "12345":
                       
                          if random_AM_time == now_time:
                                                name = adb_shell.morning()
                                                email_simple.sendmail(name,'sdfs')
                                                time.sleep(2)
                                                break
                          if random_PM_time == now_time:
                                                adb_afternoon.afternoon()
                                                time.sleep(2)
                                                break
		  time.sleep(29)

