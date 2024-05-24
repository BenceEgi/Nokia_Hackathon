import re

with open('./input.txt', 'r') as f:

  for input in f:

    input_formatted = re.sub("[^a-zA-Z0-9]", "", input).lower().strip()

    if (input_formatted == input_formatted[::-1]):
      print(f"YES, {len(set(input_formatted))}")

    else:
      print("NO, -1")