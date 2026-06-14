import time
def good_morning():
    print("Good morning!")
    time.sleep(10)  # Wait for 10 seconds
    print("Have a great day!")


good_morning()


t = time.strftime("%H:%M:%S", time.localtime())
print("Current time:", t)
hour = int(time.strftime("%H", time.localtime()))

hour = int(input("Enter the current hour (0-23): "))

if 5 <= hour < 12:
    print("Good morning!")
elif 12 <= hour < 17:
    print("Good afternoon!")
elif 17 <= hour < 21:
    print("Good evening!")
else:
    print("Good night!")