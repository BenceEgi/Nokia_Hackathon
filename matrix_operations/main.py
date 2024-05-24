from Matrix import Matrix


with open('./input.txt', 'r') as f:
  input = f.read()
#print(input)


m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]

A = Matrix(m1)
B = Matrix(m2)

print(A+B)