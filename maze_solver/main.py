import time

start = time.time()
with open('./input.txt', 'r') as f:
  input = f.read()
  input = input.split("\n")
  A = str(input[input.index("A")+1:input.index("")])[1:-1].replace(",","").replace("'", '').split(" ")
  input.remove("")
  B = str(input[input.index("B")+1:input.index("")])[1:-1].replace(",","").replace("'", '').split(" ")
  input.remove("")
  C = str(input[input.index("C")+1:input.index("")])[1:-1].replace(",","").replace("'", '').split(" ")

class Node:
  def __init__(self, x, y, values):


print(A)

def AStar():
  pass

print(time.time() - start)