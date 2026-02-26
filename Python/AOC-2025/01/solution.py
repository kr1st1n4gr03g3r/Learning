with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

print(lines[:5])  # quick sanity check