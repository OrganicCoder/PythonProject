import time
import webbrowser

totalBreaks = 3
BreaksCount = 0

print("This program started on " + time.ctime())

while BreaksCount < totalBreaks:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=Q0JBV_n60R8")
    BreaksCount = BreaksCount + 1
