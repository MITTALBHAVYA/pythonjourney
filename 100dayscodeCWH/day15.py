import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
check=int(time.strftime('%H'))
if check>=4 and check<=12 :
    print("hi sir good morning")
elif check>12 and check<13 :
    print("hi sir good noon")
elif check>=13 and check<15:
    print("hi sir good afternoon")
elif check>15 and check<=20:
    print("hi sir good evening")
else:
    print("good night")