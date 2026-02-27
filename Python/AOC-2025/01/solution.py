from pathlib import Path

lines = Path("input.txt").read_text(encoding="utf-8").splitlines()

result = []

for raw in lines:
    raw = raw.strip()
    if not raw:
        continue

    leftInput = None
    rightInput = None

    if raw.startswith("L"):
        leftInput = -int(raw[1:])     # L68 becomes integer (int) -68 
        result.append(leftInput)
    elif raw.startswith("R"):
        rightInput = int(raw[1:])     # R48 becomes integer (int) 48
        result.append(rightInput)
    else:
        raise ValueError(f"Unexpected line: {raw}")

print(result)  # [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]

zero="0"
start="50"
max="99"

