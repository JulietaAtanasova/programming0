from books import Book

def print_books(books):
  for book in books:
    print(book)

def calculate_total_price(books):
  total_price = 0;
  for book in books:
    total_price += book.price
  return total_price

def calculate_discount_price(books):
  discount = 0.25
  total_price = calculate_total_price(books)
  return total_price * discount

def find_max_books_to_buy(books, money):
  books_to_buy = []
  price = 0
  for book in books:
    price += book.price
    if price <= money:
      books_to_buy.append(book)
    else: return books_to_buy
  return books_to_buy

books = []
books.append(Book("Pragmatic Thinking and Learning", 30))
books.append(Book("Learn You a Haskell", 0))
books.append(Book("The Healthy Programmer", 50))
books.append(Book("Code Complete", 60))
books.append(Book("The Pragmatic Programmer", 20))
books.append(Book("Pro Git", 0))
books.append(Book("Introduction to Algorithms", 80))
books.append(Book("Concrete Mathematics", 100))

print_books(books)
print("The total price is: " + str(calculate_total_price(books)))
print("Books count: " + str(len(books)))
print_books(find_max_books_to_buy(books, 150))
