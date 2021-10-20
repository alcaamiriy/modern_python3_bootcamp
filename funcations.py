# x = int(input("Enter first x: "))
# y = input("Enter first y: ")


# try:
#     y = int(y)
# except:
#   print('An exception occurred')


# def multiply(x, y=10):
#     return x * y


# print(f"Result of {x}*{y} is {multiply(x)}")



# def sum_all(*args):
#   total = 0;
#   for arg in args:
#     total+= arg
  
#   return total;


# print(sum_all(1,2,3,4,5,6))


# def fav_colors(**kwargs): 
#   result = 0;
#   keys = ""
#   for key, value in kwargs.items():
#     result += value
#     keys += " " + key
#   return (keys, result)


# print(fav_colors(first=1, two=2, three=3, four=4))


nums1 = [2, 4, 6, 8, 10];

print(all(num % 2 == 0 for num in nums1))

nums2 = [1, 3, 5, 7, 9]

print(any(num % 2 != 0 for num in nums2))