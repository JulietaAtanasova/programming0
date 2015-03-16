from math import sqrt

number = int(input("Enter number: "))

def is_prime(number):
  for i in range(2,int(sqrt(number))):
    if number % i == 0:
      return False
  return True

if(is_prime(n)):
  print("The number is prime!")
else:
  print("The number is not prime!")