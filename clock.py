import time, datetime
import schedule
from threading import Thread
import alarm

# print(dir(time))


options = int (input ('Options 1 to show the time now, 2 to count down, 3 to alarm: '))

def time_func():
	print(f'{time.localtime()[3]} : {time.localtime()[4]} : {time.localtime()[5]}')


if options == 1:
	schedule.every(1).seconds.do(time_func)
	while True:
	    schedule.run_pending()
     
elif options == 2:
    print('NOT Continued')

elif options == 3:
    t = Thread(target=alarm.alarm_func)
    t.setDaemon(True)
    t.start()












 
