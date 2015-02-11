start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

def check_is_number_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

for number in range(start, end + 1):
  if check_is_number_even(number) == True:
    print(str(number) + " - even")
  else: 
    print(str(number) + " - odd")