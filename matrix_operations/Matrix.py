class Matrix:

  def __init__(self, values):
    self.row = len(values)
    self.col = len(values[0])
    self.values = values

  def __add__(self, other):

    if (self.col == other.col) and (self.row == other.row):
         return Matrix([[self.values[i][j] + other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))])

    else:
      raise Exception("Az két mátrix sorainak vagy oszlopainak hossza nem egyezik meg!")

  def __mul__(self, other):

    if (self.col == other.row):
      return Matrix([[sum(g*k for g,k in zip(m1_row,m2_col)) for m2_col in zip(*other.values)] for m1_row in self.values])

    else:
      raise Exception("Az első mátrix oszlopainak száma nem egyezik a második mátrix sorainak számával!")
