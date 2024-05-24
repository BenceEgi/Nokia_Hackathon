import itertools


class Matrix:

  def __init__(self, values):
    import itertools
    self.row = len(values)
    self.col = len(values[0])
    self.values = values

  def add(self, x, y):
    return x + y

  def __add__(self, other):
    if ((self.col == other.col) and (self.row == other.row)):
      return list(map(self.add,itertools.chain.from_iterable(self.values), itertools.chain.from_iterable(other.values)))

  def __mul__(self, other):
    pass