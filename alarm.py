import datetime, time

def alarm_func():
    alarm_time = int(input('Enter minutes to alarm on.'))
    while True:
        x = datetime.datetime.now() + datetime.timedelta(minutes=alarm_time)
        if x == datetime.datetime.now():
            print('ALARM NOW!')
   
def count_dowen(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1


t = int(input('Enter in second:'))