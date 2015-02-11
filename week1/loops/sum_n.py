end = int(input("Enter N: "))

def sum_numbers_in_interval(start, end):
  sum = 0
  for number in range(start, end + 1):
    sum += number
  return sum

print(sum_numbers_in_interval(0, end))