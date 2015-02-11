from random import randint

sides = int(input("Enter sides: "))
first_roll = random.randint(1, sides)
print("First roll:")
print(str(first_roll))

second_roll = random.randint(1, sides)
print("Second roll:")
print(str(second_roll))

third_roll = random.randint(1, sides)
print("Second roll:")
print(str(third_roll))

sum = first_roll + second_roll + third_roll
print("Sum is:")
print(str(sum))