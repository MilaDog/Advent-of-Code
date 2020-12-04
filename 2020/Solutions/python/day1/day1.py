# Day 1 - Parts 1 & 2

from sys import argv

def part1(lines):
    # looping through the list, at 'i' and at 'i+1' to see if the current and next values sum up to 2020
    for a in range(len(lines)):
        for b in range(a, len(lines)):
            if int(lines[a]) + int(lines[b]) == 2020:
                return int(lines[a])*int(lines[b])

def part2(lines):
    # looping through the list, at 'i' and at 'i+1'  and at 'i+2' to see if the current, next and next values sum up to 2020
    for a in range(len(lines)):
        for b in range(a, len(lines)):
            for c in range(b, len(lines)):
                if int(lines[a]) + int(lines[b]) + int(lines[c]) == 2020:
                    return int(lines[a]) * int(lines[b]) * int(lines[c])


def main():
    script, fileName = argv
    d1File = open(fileName, "r").read().splitlines()
    print(d1File)
    print(part1(d1File)) # 786811
    print(part2(d1File)) # 199068980

main()