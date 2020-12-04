from sys import argv

def main():
    script, fil = argv
    
    fil = open(fil, "r")
    a = [int(line.strip()) for line in fil.readlines() if line.strip()]
    
    part1 = 0
    part2 = 0

    for n1 in a:
        for n2 in a:
            if n1 + n2 == 2020:
                part1 = n1 * n2
            for n3 in a:
                if n1 + n2 + n3 == 2020:
                    part2 = n1 * n2 * n3

    print(part1)
    print(part2)

if __name__ == "__main__":
    main()