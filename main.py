import os

ENTRY_TEXT = (
    "Weekly status: emails answered, calendar defended, and I have drafted "
    "an apology to everyone you left on read in 2021. Sending Friday."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
