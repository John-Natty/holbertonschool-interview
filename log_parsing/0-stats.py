#!/usr/bin/python3
"""Parse HTTP request logs from standard input."""

import re
import sys


VALID_CODES = (
    "200", "301", "400", "401",
    "403", "404", "405", "500"
)

LOG_PATTERN = re.compile(
    r'^\S+ - \[[^]]*\] "GET /projects/260 HTTP/1\.1" '
    r'(?P<status_code>\S+) (?P<file_size>\d+)$'
)


def print_stats(total_size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))

    for code in VALID_CODES:
        if status_codes.get(code, 0) > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """Parse one log line and return status code and file size."""
    match = LOG_PATTERN.fullmatch(line.strip())

    if match is None:
        return None

    status_code = match.group("status_code")
    file_size = int(match.group("file_size"))

    return status_code, file_size


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1

            result = parse_line(line)

            if result is not None:
                status_code, file_size = result
                total_size += file_size

                if status_code in VALID_CODES:
                    status_codes[status_code] = (
                        status_codes.get(status_code, 0) + 1
                    )

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
