def count_to_number(number):
  counter = 1
  while(True):
    print(counter)
    counter += 1
    if counter == number + 1:
      break

count_to_number(60000)
print("End")