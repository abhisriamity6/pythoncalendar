import calendar
from datetime import date
from datetime import datetime
from datetime import time
monthcol = ["Jan","Feb","Mar","Apr","May","Jun","Jlu","Aug","Sept","Oct","Nov","Dec"]
mdate = datetime.now()
for m in range(1,13):
    weeksinmonth = calendar.monthcalendar(mdate.year,m)
    print("\n calendar of --> ", calendar.month_name[m])
    #print(weeksinmonth)
    for week in weeksinmonth:
        if (week[calendar.FRIDAY] != 0) :
            print("Meeting is on --> ",calendar.month_name[m],"-", week[calendar.FRIDAY])
