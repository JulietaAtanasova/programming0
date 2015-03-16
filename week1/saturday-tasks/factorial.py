n = int(input("Enter number: "))

def factorial(number):
  if number == 1 or number == 0:
    return number
  return number * factorial(number - 1)

print(factorial(n))