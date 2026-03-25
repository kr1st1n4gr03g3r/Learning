from pathlib import Path

input_file = Path("input-sample.txt").read_text(encoding="utf-8")
result = []

input_file.split('-')

print(input_file)