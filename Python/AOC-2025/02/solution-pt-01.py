from pathlib import Path

input_file = Path("input.txt").read_text(encoding="utf-8").splitlines()

result = []

print(input_file)