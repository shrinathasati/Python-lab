import datetime
from datetime import timedelta
print (datetime.datetime.now()+timedelta(days=2))

now=datetime.datetime.now()
time1=now.strftime("%H:%M:%S")
print(time1)