from pathlib import Path

src = Path("/Users/kristinagroeger/Documents/DEV-2026/temp/stupid-migration.md")
dst = Path("/Users/kristinagroeger/Documents/DEV-2026/temp/stupid-migration-paths-sorted.md")

seen = set()
out_lines = []

for line in src.read_text(encoding="utf-8").splitlines(True):  # keep newline chars
    if line not in seen:
        seen.add(line)
        out_lines.append(line)

dst.write_text("".join(out_lines), encoding="utf-8")
print(f"✅ Wrote {dst} with {len(out_lines)} unique lines")