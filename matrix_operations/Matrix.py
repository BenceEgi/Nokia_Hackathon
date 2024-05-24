class Matrix:
  def __init__(self, values):

    self.col = len(values)
    self.row = len(values[0])
    self.values = values

  def add(self, x, y):
    return x + y

  def __add__(self, other):
    if ((self.col == other.col) and (self.row == other.row)):
      return list(map(self.add,self.values, other.values))

  def __mul__(self, other):
    pass