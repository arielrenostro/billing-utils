import sys
from consts import nubank_csv_header

def validate_header(line):
    if len(line) != len(nubank_csv_header):
        print(f'Invalid header. Expected: {nubank_csv_header}, Found: {line}')
        sys.exit(1)
    
    for i in range(len(line)):
        if line[i] != nubank_csv_header[i]:
            print(f'Invalid header column {i}. Expected: {nubank_csv_header[i]}, Found: {line[i]}')
            sys.exit(1)


def validate_line(idx, line):
    if len(line) != len(nubank_csv_header):
        print(f'Invalid line size on {idx}. Expected: {len(nubank_csv_header)}, Found: {len(line)}')
        sys.exit(1)
