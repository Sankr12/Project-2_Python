import time

Hour = int(time.strftime('%H'))

if Hour>=12 and Hour<16:
    print("Good Afternoor Sir!")
elif Hour>=16 and Hour<20:
    print("Good Evening Sir!")
elif Hour>=0 and Hour<12:
    print("Good Morning Sir!")
else:
    print("Good Night Sir!")