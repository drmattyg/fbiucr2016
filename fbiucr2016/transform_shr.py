import re
import sys

DATA_LINE_REGEX = re.compile('^[\s\d]\s*\d\d')  # lines containing full or partial data match this
PARTIAL_LINE_REGEX = re.compile('^\s{37}\s*\d*')
HEADERS = "AGENCY,G,MO,HOM,INC_NUM,SIT,VA,VS,VR,VE,OA,OS,OR,OE,WEAP,REL,CIR,=]" \
          "/////////////" \
          "////////SUB,AGENCY NAME,STATE" \
    .split(",")


def is_victim(line):
    line.startswith(' ' * 37)


def is_offender(line):
    line.startswith(' ' * 51)


def main():
    process_file(sys.stdin, sys.stdout)


def process_file(input_file='data/2016 SHR FIle LIst.txt', output_file=sys.stdout):
    if type(input_file) is str:
        input_file = open(input_file, "r")
    if type(output_file) is str:
        output_file = open(output_file, "w")
    for line in input_file.readlines():
        if DATA_LINE_REGEX.search(line):
            if not PARTIAL_LINE_REGEX.search(line):
                last_full_line = line
                fields = line.split("\s*")

                print("-> " + line.strip())
            else:
                print(line.strip(), file=output_file)


if __name__ == '__main__':
    main()
