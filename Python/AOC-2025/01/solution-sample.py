from pathlib import Path

input_file = Path("input-sample.txt").read_text(encoding="utf-8").splitlines()

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

#print(result)  # [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]

########## end init

start = int(50) # start at 50
position = start 
zero_count = int(0)

# ##### Logic 01: If integer result is negative, add 100 to it
# def wrap_negative(n: int) -> int: # (n:int) means the function takes one paramater called n. the : int part is a type hint saying you expect n to be an integer
#     if n < 0: # If integer is negative
#         n += 100 # Add 100 to integer
#     return n # Return integer

# #print(wrap_negative(test))

# ##### Logic 02: If the integer position is exactly 100, reset number to 0
# def position_hundred(n: int) -> int:
#     if n == 100: # If the integer position is exactly 100
#         n = int(0) # Reset the integer to 0
#     return n   
    
#print(position_hundred(test))

##### Logic 03: If the position integer starts at zero, add 1
def position_zero(n: int) -> int:
    global zero_count
    if n == 0:
        zero_count += 1 # Increment zero_count by 1 each time it lands on zero
        # n += 1
    return n

##### Logic 04: If the integer is over 100, use modulo
def position_over_hundred(n: int) -> int:
    return n % 100

for move in result:
    position = position + move
    position = position_over_hundred(position)
    position = position_zero(position)

print(position)
print(zero_count)