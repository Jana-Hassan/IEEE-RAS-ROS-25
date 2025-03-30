import datetime
Day = int(input("Day:"))
Month = int(input("Month:"))
Year = int(input("Year:"))

Today = datetime.date(Year, Month, Day)
Tommorow = Today + datetime.timedelta(days=1)

print("Day:",Tommorow.day, "Month:", Tommorow.month, "Year:",Tommorow.year)