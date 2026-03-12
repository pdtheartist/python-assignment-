seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month number: "))

if month == 12 or month == 1 or month == 2:
    print("Season:", seasons[0])

elif month == 3 or month == 4 or month == 5:
    print("Season:", seasons[1])

elif month == 6 or month == 7 or month == 8:
    print("Season:", seasons[2])

elif month == 9 or month == 10 or month == 11:
    print("Season:", seasons[3])