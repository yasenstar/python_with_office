from datetime import datetime

dt_now = datetime.now()
print(type(dt_now), dt_now)

print(dt_now.year, dt_now.month, dt_now.day, type(dt_now.year))

print(dt_now.hour, dt_now.minute, dt_now.second, dt_now.microsecond, type(dt_now.hour))