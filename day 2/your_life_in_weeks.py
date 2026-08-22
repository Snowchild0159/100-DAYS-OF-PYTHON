age = input("What is your current age? ")
years_remaining = 90 - int(age)
months_remaining = (90 - int(age)) * 12
weeks_remaining = (90 - int(age)) * 52
days_remaining = (90 - int(age)) * 365

print(f"you have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, and {days_remaining} days left.")