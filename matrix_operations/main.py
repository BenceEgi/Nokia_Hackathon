from Matrix import Matrix
from re import match, split

with open('./input.txt', 'r') as f:
  input = f.read()
  input = input.strip().split("\n")[2::]

list = []
variable_name = ""
execute = False

for i in input:

    if execute:

      if (i != ""):
        exec(f"result = {i}")
        print(i)

        for j in result.values:
          print(*j)

      print("")

    elif i == 'operations':
      execute = True

    elif i == '':
      exec(f"{variable_name} = Matrix({list})")
      list = []

    elif match("[a-zA-Z]", i):
      variable_name = i

    elif match('[0-9]', i):
      list.append([int(k) for k in split("[ ]+", i)])