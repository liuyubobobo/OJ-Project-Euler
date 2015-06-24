def isLeapYear( year ):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def daysFrom1900( year , month , day ):

    nonLeapYearDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    leapYearDays    = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    days = 0
    for y in range(1900,year):
        days += 366 if isLeapYear( y ) else 365

    if isLeapYear( year ):
        monthDays = leapYearDays
    else:
        monthDays = nonLeapYearDays

    days += sum( monthDays[0:month] )
    days += day
    return days
        
    
    
if __name__ == "__main__":
    
    res = 0
    for year in range(1901,2001):
        for month in range(1,13):
            res += 1 if daysFrom1900( year , month ,1 )%7 == 0 else 0
    print( res )
        
