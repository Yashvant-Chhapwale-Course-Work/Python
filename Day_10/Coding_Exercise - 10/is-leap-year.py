def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        
#-------------------------------------------------------------------------------------------------------------------------------------------------#
year = int(input("Enter A Year: "))

if is_leap_year(year) == True and year % 1000 == 0:
    print(f"The Year {year} is a Millenial Leap Year.") 
elif is_leap_year(year) == True and year % 400 == 0:
    print(f"The Year {year} is a Centurial Leap Year.")
elif is_leap_year(year) == True:
    print(f"The Year {year} is a Leap Year.")
else:
    print(f"The Year {year} is not a Leap Year.")


# Logic: 
#   - Every Year Divisible By 4 is a 'Leap Year'
#   - Unless The Year is also Divisible By 100, Then it is not a 'Leap Year' 
#   - But if it is Divisible by 100 & also by 400, Then it is a 'Centurial Leap Year (1600, 2000, 2400, etc)' or sometimes a 'Millenial Leap Year (2000, 4000, 8000, etc)'