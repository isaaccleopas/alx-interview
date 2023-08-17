#!/usr/bin/python3
"""reads stdin line by line and computes metrics:"""
import sys
import signal

status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0

def print_statistics(signal, frame):
    """calculates statistics"""
    global total_file_size
    global line_count
    print("File size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
    total_file_size = 0
    line_count = 0

signal.signal(signal.SIGINT, print_statistics)

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) == 7:
        try:
            status_code = int(parts[5])
            file_size = int(parts[6])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
        except ValueError:
            pass

        if line_count % 10 == 0:
            print_statistics(None, None)
