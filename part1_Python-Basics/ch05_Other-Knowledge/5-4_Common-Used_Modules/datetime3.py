from datetime import datetime

dt_now = datetime.now()
fmt_str = "%Y-%B-%d %I:%M:%S %p %A "

dt_now_str = dt_now.strftime(fmt_str)

print(type(dt_now_str),dt_now_str)

dt = datetime.strptime(dt_now_str,fmt_str)
print(type(dt), dt)