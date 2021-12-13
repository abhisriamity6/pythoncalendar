import calendar
mycal = calendar.TextCalendar(calendar.MONDAY)
for cal in mycal.itermonthdates(2021,8):
    print(cal)




#print(mycal.formatyear(2021))