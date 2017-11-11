import re
import sys

DATA_LINE_REGEX = re.compile('^[\s\d]\s*\d\d')  # lines containing full or partial data match this
PARTIAL_LINE_REGEX = re.compile('^\s{37}\s*\d*')


def main():
    for line in sys.stdin:
        if DATA_LINE_REGEX.search(line):
            if PARTIAL_LINE_REGEX.search(line):
                print("-> " + line.strip())
            else:
                print(line.strip())


if __name__ == '__main__':
    main()
