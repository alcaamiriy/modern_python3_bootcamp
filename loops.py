# times = input("how many times do I have to you?: ")

# for scream in range(int(times)):
#     print("clean up your room!".upper())


# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f"{num} is UNLUCKY")
#     elif num % 2 == 0:
#         print(f"{num} is EVEN")
#     else:
#         print(f"{num} is ODD")


# input("Press any key to exist ...")
# exit(0)

print("Printing emojis with FOR loop")
for row in range(1, 11):
    print("\U0001f610" * row)

print()
print()

print("Printing emojis with FOR loop")
for row in range(1, 11):
    col = row
    while col >= row:
        print("\U0001f600" * col)
        col -= 1

print()
print()

print("Printing emojis with WHILE loop")
rows = 10
while rows >= 1:
    print("\U0001f601" * rows)
    rows -= 1
