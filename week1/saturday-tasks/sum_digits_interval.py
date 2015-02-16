n = int(input("Enter n: "))
m = int(input("Enter m: "))

def sum_digits(number):
  sum = 0
  while number > 0:
    sum += number % 10
    number //= 10
  return sum

for number in range(n, m + 1):
  print("Sum of digits of %s = %s" % (number, sum_digits(number)))