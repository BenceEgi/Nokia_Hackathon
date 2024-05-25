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

def Solve(Maze:list, height:int, start, goal, step:list):
  GOAL = goal
  START = start
  searcher = START
  steps = step
  values = []
  possible_steps = []


  if (searcher == GOAL):
    steps.append("G")
    print(steps)
    return steps

  if (Maze[searcher - 1] == '#'):
      pass

  elif ((Maze[searcher - 1] in '.G') and (steps[-1] != "R")):
      possible_steps.append("L")
      values.append((searcher - 1))

  if (Maze[searcher + 1] == '#'):
      pass

  elif ((Maze[searcher + 1] in '.G') and (steps[-1] != "L")):
      possible_steps.append("R")
      values.append((searcher + 1))

  if (Maze[searcher-(len(Maze)//height)] == "#"):
      pass

  elif ((Maze[searcher-(len(Maze)//height)] in ".G") and (steps[-1] != "D")):
      possible_steps.append("U")
      values.append((searcher - (len(Maze)//height)))

  if (Maze[searcher+(len(Maze)//height)] == "#"):
      pass

  elif ((Maze[searcher+(len(Maze)//height)] in ".G") and (steps[-1] != "U")):
      possible_steps.append("D")
      values.append((searcher + (len(Maze)//height)))

  print(possible_steps)
  print(values)

  if (GOAL > START):
    steps.append(possible_steps[values.index(min(values, key=lambda x: abs(GOAL - x)))])
    searcher = values[values.index(min(values, key=lambda x: abs(GOAL - x)))]
    print(min(values, key=lambda x: abs(GOAL - x)))
  else:
    steps.append(possible_steps[values.index(max(values, key=lambda x: abs(GOAL - x)))])
    print(max(values, key=lambda x: abs(GOAL - x)))
    searcher = values[values.index(max(values, key=lambda x: abs(GOAL - x)))]

  Solve(Maze, height, searcher, goal, steps)

print(C.index("G"))
Solve(B, 10, B.index("S"), B.index("G"), ["S"])
#Solve(C, 15, C.index("S"), C.index("G"), ["S"])

print(time.time() - start)