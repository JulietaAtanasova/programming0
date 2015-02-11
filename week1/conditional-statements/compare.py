a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
  print("a(" + str(a) + ") is bigger than b(" + str(b) + ")!")
elif b > a:
  print("b(" + str(b) + ") is bigger than a(" + str(a) + ")!")
elif a == b:
  print("a(" + str(a) + ") is equal to b(" + str(b) + ")")