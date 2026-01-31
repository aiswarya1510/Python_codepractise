def leapyear(year):
    if year%400==0:
        return "It is a leap Year"
    elif year%4==0 and year%100!=0:
        return "It is a leap year"
    else:
        return "It is not a leap year"
    

print(leapyear(1900))