##webbbrowser and time are modules inside the python standard library...both modules have several functions that we can use to perform task
###we just have to import the modules and then use it functions
import webbrowser
import time

"""def take_break():
    print("timer starts at"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/user/Udacity")
take_break()
take_break()
take_break()"""

                                ###using while loops

"""total_breaks = 3
break_counter = 0
print("this program started on " + time.ctime())
while (break_counter < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=uGjsDGqQsSk")
    break_counter = break_counter + 1"""
                                  ###using for loops
"""for i in range(3):
    print("this program started on " + time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=uGjsDGqQsSk")"""
total=0
for i in range(3):
    total+=i
    i+=1
print(total)




