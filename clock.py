# Python DataTime

# import datetime as dt

# tim = dt.datetime.now()
# print(tim)
# print(tim.date())
# print(tim.time())
# print(tim.year)
# print(tim.month)
# print(tim.day)
# print(tim.hour)
# print(tim.minute)
# print(tim.second)

# tm = dt.datetime(2023, 12, 25)
# # print(tm)
# # print(tm.month)
# tm = dt.datetime(2023, 4, 10, 12, 30, 20)
# print(tm)

# # Example(countdown)
# while True:
#     current_date = dt.datetime.now()
#     if current_date.second == 0 and current_date.minute == 15 and current_date.strftime("%p")=="PM":
#         future_date = dt.datetime(2023, 12, 7)
#         current_date = dt.datetime.now()
#         day = future_date.date() - current_date.date()
#         print(day.days, " days left" )


# strftime() method - use to format datetime object into readable string

# tim = dt.datetime.now()
# print(tim.strftime("%A"))
# print(tim.strftime("%B"))
# print(tim.strftime("%w"))

# # strftime format codes
# %a : returns weekday in short version eg wed
# %A : returns weekday in full version eg wednesday
# %w : returns weekday in number version from 0-6 where 0 means sunday eg web is 3 
# %d : returns day of the month in number version from 01-31
# %b : returns month name in short version eg Dec
# %B : returns month name in full version eg December
# %m : returns month in number formart from 01-12 
# %y : returns year in short version eg 2021 is 21
# %Y : returns year in full version eg 2021
# %H : returns hour in 24hrs format from 00-23
# %I : returns hour in 12hrs format from 00-12
# %p : returns AM or PM of time
# %M : returns minute of time from 00-59
# %S : returns seconds of time from 00-59
# %f : returns microseconds of time from 000000-999999
# %Z : for timezone
# %j : days number of the year from 001-366
# %U : return week number of the year from 00-54 

# tm = dt.datetime.now()
# print(tm.strftime("%B"))

# Example 2

# while True:
#     tm = dt.datetime.now()

#     if tm.strftime("%I") == "11" and tm.strftime("%M") == "04" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
#         print("Its time to play.")

# Example 3      
# import datetime
# check = int(datetime.datetime.now().strftime("%M"))
# rang =[rn for rn in range(0,60)]

# while True:
#     time =datetime.datetime.now() 
#     nexttime = time.strftime('%M')
#     if int(nexttime) in rang and check == int(nexttime):   
#         for i in range(5):
#             print("i am going for class today")
#     check = int(nexttime )+ 1




# Python Math class
import math, cmath
# l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(5, 3))

# print(math.sqrt(9))
# print(math.ceil(6.3492))
# print(math.floor(5.6732))
# print(round(5.32))
# print(round(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)
# print(math.comb(16, 4))
# print(math.comb.__doc__)