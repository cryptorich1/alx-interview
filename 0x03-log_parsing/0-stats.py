import sys

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()

            if len(parts) != 7:
                # Skip lines with invalid format
                continue

            ip_address, _, _, _, status_code_str, file_size_str, *_ = parts

            try:
                status_code = int(status_code_str)
                file_size = int(file_size_str)
            except ValueError:
                # Skip lines with invalid status code or file size
                continue

            total_size += file_size
            status_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
