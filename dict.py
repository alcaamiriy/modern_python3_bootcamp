print()
obj = {
    "firstname": "John",
    "lastname": "Doe",
    "age": 52
}
print(obj)

print()
car = dict({
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
})

car_keys = car.keys()
car_values = car.values()

print()
print(f"Car keys are: {car_keys}")
print()
print(f"Car values are: {car_values}")

print()
for item in car.items():
    print(f"{item}")

print()
if "brand" in car:
    print("There is brand in the KEYS")

print()
if "Ford" in car.values():
    print("There is 'Ford' value in the VALUES")
