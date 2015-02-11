a = float(input("Lower bound of the interval: "))
b = float(input("Upper bound of the interval: "))
x = float(input("Enter number: "))

if x == a:
  print("The number is equal to the lower bound of the interval")
elif x == b:
  print("The number is equal to the upper bound of the interval")
elif a < x < b:
  print("The number is in the interval")
elif x < a:
  print("The number is outside the interval, x < a")
elif x > b:
  print("The number is outside the interval, x > b")