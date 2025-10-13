# write your code here
def is_valid_month(month):
    if month<=12 and month>0:
        return True
    return False
def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False
def has_30_days(month): #Note: `has_30_days(month)` should return `False` of months with more than `30` days.
    if month==4 or month==6  or month==9 or month==11:
        return True
    return False
def has_31_days(month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return True
    return False
def has_28_days(month, year):
    if month==2 and False==is_leap_year(year):
        return True
    return False
def has_29_days(month, year):
    if month==2 and True==is_leap_year(year):
        return True
    return False
def is_valid_date(day, month, year):
    if not is_valid_month(month):
        return False
    if has_31_days(month) and 1 <= day <= 31:
        return True
    elif has_30_days(month) and 1 <= day <= 30:
        return True
    elif has_29_days(month, year) and 1 <= day <= 29:
        return True
    elif has_28_days(month, year) and 1 <= day <= 28:
        return True
        
    return False