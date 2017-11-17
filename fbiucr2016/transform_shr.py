import re
import sys

DATA_LINE_REGEX = re.compile('^[\s\d]\s*\d\d')  # lines containing full or partial data match this
PARTIAL_LINE_REGEX = re.compile('^\s{37}\s*\d*')
HEADERS = "AGENCY,G,MO,HOM,INC_NUM,SIT,VA,VS,VR,VE,OA,OS,OR,OE,WEAP,REL,CIR,SUB,AGENCY NAME,STATE" \
    .split(",")
FIELD_OFFSETS = [5, 16, 18, 22, 27, 33, 38, 42, 45, 48, 52, 56, 59, 62, 66, 72, 77, 82, 86, 112]
assert (len(HEADERS) == len(FIELD_OFFSETS))  # need to check this before moving on


def is_victim(line):
    return line.startswith(' ' * 37)


def is_offender(line):
    return line.startswith(' ' * 51)


def main():
    process_file(sys.stdin, sys.stdout)


def process_file(input_file='data/2016 SHR FIle LIst.txt', output_file=sys.stdout):
    if type(input_file) is str:
        input_file = open(input_file, "r")
    if type(output_file) is str:
        output_file = open(output_file, "w")
    for line in input_file.readlines():
        fields = re.split("\s*", line.strip())
        if DATA_LINE_REGEX.search(line):
            if not PARTIAL_LINE_REGEX.search(line):
                last_full_fields = fields
            else:
                if is_offender(line):
                    pass
                    # handle this


if __name__ == '__main__':
    main()
