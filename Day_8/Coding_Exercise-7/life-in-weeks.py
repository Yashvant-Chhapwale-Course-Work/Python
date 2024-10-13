age = int(input("Enter Your Age:"))

def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52    #1 Year = 52 Weeks
    print(f"You have {weeks_left} Weeks left i.e {years_left} more Years !")

life_in_weeks(age)