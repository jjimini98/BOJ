# 2007 년
import  sys
import calendar


month, date = map(int, sys.stdin.readline().split(" "))


if calendar.weekday(2007,month,date) ==0 :
    print("MON")
elif calendar.weekday(2007,month,date)==1:
    print("TUE")
elif calendar.weekday(2007,month,date) ==2:
    print("WED")
elif calendar.weekday(2007,month,date) ==3:
    print("THU")
elif calendar.weekday(2007,month,date) ==4:
    print("FRI")
elif calendar.weekday(2007,month,date) ==5:
    print("SAT")
else :
    print("SUN")
