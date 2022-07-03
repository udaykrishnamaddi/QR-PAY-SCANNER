from datetime import datetime

date = '03/07/2022'
time = '16:32:30'

date_list = date.split('/')
time_list = time.split(':')

generated = datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]), int(time_list[0]), int(time_list[1]), int(time_list[2]))
now = datetime.now()

difference = now - generated
duration_in_seconds = difference.total_seconds()

minutes = divmod(duration_in_seconds, 60)[0]
print(minutes)