a = float(input("Enter a: "))
b = float(input("Enter b: "))
oper = input("Enter operation: ")

if oper == "+":
  result = a + b
  print("Result is:")
elif oper == "-":
  result = a - b
  print("Result is:")
elif oper == "*":
  result = a * b
  print("Result is:")
elif oper == "/":
  result = a / b
  print("Result is:")
else: 
  result = "We do not support that operation"

print("%.2f" % result)