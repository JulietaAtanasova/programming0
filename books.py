class Book(object):
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __repr__(self):
    return "Name: " + self.name + ", Price: " + str(self.price)