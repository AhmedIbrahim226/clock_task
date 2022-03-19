import datetime, time


def alarm_func(alarm_time):
    x1 = datetime.datetime.now() + datetime.timedelta(seconds=alarm_time)

    while True:
        if str(x1.ctime()) == str(datetime.datetime.now().ctime()) :
            print('ALARM NOW!')
            break

def count_dowen(t):
    while t:
        mints, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mints, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1


