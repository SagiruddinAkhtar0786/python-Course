import time
Time = time.localtime()
Hour = Time.tm_hour 
minute = Time.tm_min
indianTime = (Hour + 5) % 24
indianMinute = (minute + 30) % 60   

print("Good Morning, it's currently " + str(Hour) + ":" + str(minute) + " o'clock")
print("In Indian time, it's currently " + str(indianTime) + ":" + str(indianMinute) + " o'clock")


timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Current timestamp: ", timestamp)