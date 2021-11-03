def is_year_leap(year):
    if year < 1528:
        return("not within the geogian calander")
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 30, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        if month == 2:
            return 29
    return months[month - 1]
#
# Your code from LAB 4.3.1.7.
#

def day_of_year(year, month, day):
    if year < 1528:
        return None
    if month > 12 or month < 1:
        return None
    if day > 31 or day < 1:
        return None
        
        
    total = day
    month = month - 1
    while month > 0:
       total += days_in_month(year, month)
       month -= 1
    return total
    
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
