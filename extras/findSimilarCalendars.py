birth_year = int(input("enter your birth year: "))
age = int(input("how many years do you want to live: "))

death_year = birth_year + age

calendar_repeats = [birth_year]
while True:
    remainder = calendar_repeats[-1] % 4
    
    if remainder == 0:
        calendar_repeats.append(calendar_repeats[-1] + 28)
    elif remainder == 1:
        calendar_repeats.append(calendar_repeats[-1] + 6)
    elif remainder == 2:
        calendar_repeats.append(calendar_repeats[-1] + 11)
    else:
        calendar_repeats.append(calendar_repeats[-1] + 11)
    
    if calendar_repeats[-1] > death_year:
        break
    
print(f"\nYou will see { len(calendar_repeats) - 1 } years will same calendar as your birth year")
for i in range(1, len(calendar_repeats)):
    print(f" {i}: {calendar_repeats[i]}")