n = int(input("Enter n: "))
m = int(input("Enter m: "))

n_last_digit = n % 10
m_last_digit = m % 10

if n_last_digit > m_last_digit:
  print(n)
elif n_last_digit < m_last_digit:
  print(m)
elif n > m:
  print(n)
else:
  print(m)