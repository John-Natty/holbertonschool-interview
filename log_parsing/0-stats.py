#!/usr/bin/python3
"""Log parsing module."""

import sys


def print_stats(total_size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size

                if status_code in valid_codes:
                    status_codes[status_code] = (
                        status_codes.get(status_code, 0) + 1)

            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
