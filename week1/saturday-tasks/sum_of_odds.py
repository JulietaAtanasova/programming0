n = int(input("Enter number: "))

sum = 0

for number in range(1, n + 1):
  if number % 2 == 1:
    sum += number

print("Sum of odds: " + str(sum))