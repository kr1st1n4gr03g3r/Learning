from pathlib import Path

input_file = Path("input-sample.txt").read_text(encoding="utf-8")
result = []

data = input_file # Take in the integers
split_them = data.split(",") # Split them in a new line after ","

a, b = split_them[0].split("-") #.split() returns a list, and Python lists are zero-indexed (first item is index 0)

range_start = int(a) # start at first number
range_end = int(b) # end at last number

for i in range(range_start, range_end +1):

        print(i)
