#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def signal_handler(sig, frame):
    """Handle a keyboard interrupt signal (Ctrl+C) and print stats before exiting."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read input line by line
for line in sys.stdin:
    line_count += 1

    try:
        parts = line.split()
        if len(parts) >= 7:
            ip = parts[0]
            status_code = parts[-2]
            file_size = parts[-1]

            # Update the file size
            total_size += int(file_size)

            # Update the status code count if it is a valid code
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        if line_count % 10 == 0:
            print_stats()
    except Exception:
        pass

# Print final statistics when the input ends
print_stats()
