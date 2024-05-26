from collections import deque
from re import split

with open('./input.txt', 'r') as f:
  input = f.read()
  input = input.split("\n")

  A = [split(" ", i) for i in input[input.index("A")+1:input.index("")]]

  input.remove("")

  B = [split(" ", i) for i in input[input.index("B")+1:input.index("")]]

  input.remove("")

  C = [split(" ", i) for i in input[input.index("C")+1:input.index("")]]

def solve(maze):
  Row = len(maze)
  Col = len(maze[0])

  start = [(row, col) for col in range(Col) for row in range(Row) if (maze[row][col] == "S")]

  My_Queue = deque()
  My_Queue.appendleft((start[0][0], start[0][1], "S "))

  Directions = [[0,1], [0,-1], [1,0], [-1,0]]
  visited = [[False] * Col for i in range(Row)]

  while len(My_Queue) != 0:
    coordinate = My_Queue.pop()
    visited[coordinate[0]][coordinate[1]] = True

    if maze[coordinate[0]][coordinate[1]] == "G":
        return coordinate[2]+"G"

    for dir in Directions:
        newRow = coordinate[0]+dir[0]
        newCol = coordinate[1]+dir[1]

        if newRow < 0 or newRow >= Row or newCol < 0 or newCol >= Col or maze[newRow][newCol] == "#" or visited[newRow][newCol]:
            continue

        if dir == [0,1]:
            My_Queue.appendleft((newRow, newCol, coordinate[2] + "R "))

        elif dir == [0,-1]:
            My_Queue.appendleft((newRow, newCol, coordinate[2] + "L "))

        elif dir == [1, 0]:
            My_Queue.appendleft((newRow, newCol, coordinate[2] + "D "))

        elif dir == [-1, 0]:
            My_Queue.appendleft((newRow, newCol, coordinate[2] + "U "))


print("A\n" + solve(A) + "\n")

print("B\n" + solve(B) + "\n")

print("C\n" + solve(C) + "\n")