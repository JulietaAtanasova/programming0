import time

today = time.strftime("%A")

if today == "Friday":
  print("It is friday!")
else:
  print("It is not friday ;( Today is " + today + ".")