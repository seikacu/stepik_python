minutes = int(input())
minutes_on_hour = 60
hour = minutes // minutes_on_hour
ost_minutes = minutes % minutes_on_hour
print(minutes, 'мин - это', hour, 'час', ost_minutes, 'минут', end='.')
