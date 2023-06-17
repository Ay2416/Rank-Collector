import datetime

time = "2023-06-10 07:38:23.676284"
time_format = '%Y-%m-%d %H:%M:%S.%f'

change = datetime.datetime.strptime(time, time_format)

now = datetime.datetime.now()

calc = now - change

print(calc.total_seconds())