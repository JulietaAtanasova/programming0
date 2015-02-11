min_grade = 0
max_grade = 100

grade = int(input("Enter grade: "))

if min_grade <= grade <= (max_grade // 2):
  print("Слаб 2")
elif (max_grade // 2 + 1) <= grade <= (max_grade // 2 + 10):
  print("Среден 3")
elif (max_grade // 2 + 11) <= grade <= (max_grade // 2 + 20):
  print("Добър 4")
elif (max_grade // 2 + 21) <= grade <= (max_grade // 2 + 30):
  print("Много Добър 5")
elif (max_grade // 2 + 31) <= grade < max_grade:
  print("Отличен 6")
elif grade == max_grade:
  print("Много отличен 7")