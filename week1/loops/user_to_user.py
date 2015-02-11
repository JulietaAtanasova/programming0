start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

def count_from_start_to_end(start, end):
  for number in range(start, end + 1):
    print(number)

count_from_start_to_end(start, end)