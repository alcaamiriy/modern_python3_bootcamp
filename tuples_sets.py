
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")

print(type(months))


print()

for month in months:
    print(month)

print()
print("Backwards")
length = len(months)
while length > 0:
    print(months[length - 1])
    length -= 1
