from pathlib import Path

input_file = Path("input.txt").read_text(encoding="utf-8").splitlines()

result = []

for raw in input_file:
    raw = raw.strip()
    if not raw:
        continue ## Checks if string is empty

    anti_clockwise = None
    clockwise = None

    if raw.startswith("L"):
        anti_clockwise = -int(raw[1:])     # L68 becomes integer (int) -68 
        result.append(anti_clockwise)
    elif raw.startswith("R"):
        clockwise = int(raw[1:])     # R48 becomes integer (int) 48
        result.append(clockwise)
    else:
        raise ValueError(f"Unexpected line: {raw}")

########## end init

start = int(50) # start at 50
position = start 
zero_count = int(0)

##### Logic 01: If the position integer starts at zero, add 1
def position_zero(n: int) -> int:
    global zero_count
    if n == 0:
        zero_count += 1 # Increment zero_count by 1 each time it lands on zero
        # n += 1
    return n

##### Logic 02: If the integer is over 100, use modulo
def position_over_hundred(n: int) -> int:
    return n % 100

# for move in result:
#     position = position + move
#     position = position_over_hundred(position)
#     position = position_zero(position)


for move in result:
    direction = 1 if move > 0 else -1 # direction variable is equal to 1 if the move is to the right  (> 0 ) otherwise, direction is -1.
    steps = abs(move) # Absolute value of move, the result will always be non-negative. -5 will result as 5. 0 will result as 0.

    for _ in range(steps):
        position = position + direction
        position = position_over_hundred(position)
        position = position_zero(position)

print(position)
print(zero_count)