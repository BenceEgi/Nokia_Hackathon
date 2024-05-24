from Matrix import Matrix

with open('./input.txt', 'r') as f:
  input = f.read()
#print(input)


m1 = [[1,2,3],
      [3,4,3]]

m2 = [[5,6,4],
      [7,8,5]]

A = Matrix(m1)
B = Matrix(m2)

print(A+B)