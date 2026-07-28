"""One-off script to crop figures from PDF page renders."""

from __future__ import annotations

from scripts.figure_crop_ops import crop_all_figures


def main() -> None:
    for message in crop_all_figures():
        print(message)


if __name__ == "__main__":
    main()
