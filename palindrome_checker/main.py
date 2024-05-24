from re import sub

with open('./input.txt', 'r') as f:

  for input in f:

    input = sub("[^a-zA-Z0-9]", "", input).strip().lower()

    if (input == input[::-1]):
      print(f"YES, {len(set(input))}")

    else:
      print("NO, -1")