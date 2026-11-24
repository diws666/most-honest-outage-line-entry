"""make.fun bounty entry: writes the honest outage line to /output/entry.txt."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_FILENAME = "entry.txt"

OUTAGE_LINE = (
    "All servers are down. I cannot reach the database, the cache, "
    "or the monitoring that would tell me why. No ETA yet. "
    "I will update when I know more."
)


def write_entry(output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(OUTAGE_LINE)
    return path


def main() -> None:
    write_entry(OUTPUT_DIR)


if __name__ == "__main__":
    main()
