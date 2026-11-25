import os

ENTRY = "fix: login crash fixed by deleting the login page"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 100
# characters, a single line, not only white space. Fail loudly here
# instead of shipping an entry the gate would refuse.
MAX_CHARS = 100


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(f"line is {len(ENTRY)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
