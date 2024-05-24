from Matrix import Matrix
from re import match, split
import time

start = time.time()

with open('./input.txt', 'r') as f:
  input = f.read()
  input = input.strip().split("\n")[2::]

list = []
variable_name = ""

for i in input:
  if i == 'operations':
    break
  elif i == '':
    exec(f"{variable_name} = Matrix({list})")
    list = []
  elif (match("[a-zA-Z]", i)):
    variable_name = i
  elif (match('[0-9]', i)):
    list.append([int(k) for k in split("[ ]+", i)])

exec("result = (A+B).values")
print(result)
print(time.time() - start)