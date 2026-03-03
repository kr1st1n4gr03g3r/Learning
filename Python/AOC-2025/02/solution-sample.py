from pathlib import Path

input_file = Path("input-sample.txt").read_text(encoding="utf-8")
result = []

data = input_file
split_them = data.split(",")
print(split_them)

a, b = split_them[0].split("-") #.split() returns a list, and Python lists are zero-indexed (first item is index 0)
range_start = int(a)
range_end = int(b)