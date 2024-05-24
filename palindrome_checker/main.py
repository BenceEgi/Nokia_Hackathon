from re import sub

with open('./input.txt', 'r') as f:

    for i in f:

        input_formatted = sub("[^a-zA-Z0-9]", "", i).strip().lower()

        if input_formatted == input_formatted[::-1]:
            print(f"YES, {len(set(input_formatted))}")

        else:
            print("NO, -1")

