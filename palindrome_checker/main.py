from re import sub
import time

start = time.time()

with open('./input.txt', 'r') as f:

    for input in f:

        input_formatted = ''.join(filter(str.isalnum, input)).strip().lower()

        if input_formatted == input_formatted[::-1]:
            print(f"YES, {len(set(input_formatted))}")
        else:
            print("NO, -1")

print(time.time() - start)