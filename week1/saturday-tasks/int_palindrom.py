n = int(input("Enter number: "))

def is_palindrom(number):
  reversed_number = int(''.join(reversed(str(number))))
  if number == reversed_number:
    return True
  else: 
    return False

if is_palindrom(n):
  print("The number is palindrom")
else:
  print("The number is not palindrom")
