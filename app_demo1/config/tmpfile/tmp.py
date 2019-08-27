import datetime,time
start_time=datetime.datetime.now()
time.sleep(5)
end_time = datetime.datetime.now()


print(start_time)
print(end_time)
print(type(start_time))
print(end_time-start_time)
print(0+(end_time-start_time))
print((end_time-start_time)+(end_time-start_time))