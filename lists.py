colors = ["black", "blue", "purple"]

print(f"Is 'Green' i the colors? { 'green' in colors }")
print()
print(f"Is 'Black' in the colors? { 'black' in colors }")

color = input("Add color to the colors: ")

colors.append(color)

colors.sort()
print(colors)


num = [16, 25, 36, 49, 64]

print([x ** .5 for x in num])


name = "amir"

print("".join([y.upper() for y in name]))
