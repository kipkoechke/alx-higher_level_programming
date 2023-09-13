#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            try:
                parts = line.split()
                size = int(parts[-1])
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
                total_size += size

                if count == 10:
                    print_stats(total_size, status_codes)
                    count = 0
            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
