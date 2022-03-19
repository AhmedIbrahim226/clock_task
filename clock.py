import time, datetime
import schedule
from threading import Thread
import alarm


options = int (input ('Options 1 to show the time now, 2 to count down, 3 to alarm: '))

def time_func():
    print(f'{time.localtime()[3]} : {time.localtime()[4]} : {time.localtime()[5]}')


if options == 1:
    schedule.every(1).seconds.do(time_func)
    while True:
        schedule.run_pending()
     
elif options == 2:
   t = int(input('Enter in second:'))
   alarm.count_dowen(t)

elif options == 3:
    alarm_time = int(input('Enter seconds to alarm on: '))
    Thread(target=alarm.alarm_func, args=[alarm_time]).start()












 
