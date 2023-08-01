import time

print("\n\n ************ Water Reminder ************\n\n")

Time = time.time()
current_time = time.ctime(Time)

print("Current Time is :- " , current_time)
print("I hope that you have drink water now!!! I will remind you after every 30 minutes that you have to drink water!!!")

while True:
    time.sleep(1800) # because 30 min = 30*60 sec = 1800 sec
    print("Hello! It's Time to drink Water!!!!")
  