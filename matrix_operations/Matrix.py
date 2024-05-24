class Matrix:

  def __init__(self, values):
    self.row = len(values)
    self.col = len(values[0])
    self.values = values

  def add(self, x, y):
    return x + y
  def __add__(self, other):
    import itertools
    final = []
    if (self.col == other.col) and (self.row == other.row):
         result = list(map(self.add,itertools.chain.from_iterable(self.values), itertools.chain.from_iterable(other.values)))
         for i in range(self.row):
             final.append(result[:self.col])
             result = result[self.col:]
         return Matrix(final)

  def multiply(self, *args):
    print(args)
  def __mul__(self, other):
      import itertools
      final = []
      if (self.col == other.col) and (self.row == other.row):
          result = list(
              map(self.multiply, self.values, other.values))
          for i in range(self.row):
              final.append(result[:self.col])
              result = result[self.col:]
          return Matrix(final)