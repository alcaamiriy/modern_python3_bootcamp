choice = input("To convert KM to MI enter 1 or to convert MI to KM enter 2: ")
print()
ONE_MILE = 0.621371192
result = 0
unit = None
converted_unit = None
if int(choice) == 1:
    distance = input("How many Kilometers have you run this week?: ")
    unit = "KMs"
    converted_unit = "MIs"
    result = round(float(distance) * ONE_MILE, 2)
else:
    distance = input("How many Miles have you run this week?: ")
    unit = "MIs"
    converted_unit = "KMs"
    result = round(float(distance) / ONE_MILE, 2)


print()
print(f"You run {distance}{unit} this week which is equal to {result}{converted_unit}")
print()
