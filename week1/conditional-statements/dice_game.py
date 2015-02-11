from random import randint

sides = int(input("Enter dice side: "))

first_player = input("Enter player1 name: ")
second_player = input("Enter player2 name: ")

first_player_roll = randint(1, sides)
second_player_roll = randint(1, sides)

print(first_player + " rolls " + str(first_player_roll))
print(second_player + " rolls " + str(second_player_roll))

if first_player_roll > second_player_roll:
  print(first_player + " wins!")
elif second_player_roll > first_player_roll:
  print(second_player + " wins!")
else:
  print("Draw")