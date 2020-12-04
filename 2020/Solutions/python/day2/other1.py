from sys import argv

def main():
    script, fil = argv
    fin = open(fil, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()] # removing ahead & trailing whitespaces - making a list

    part1, part2 = 0, 0
    for line in lines:
        rng, chck, pwd = line.split() # getting the parts to work with
        chck = chck[0] # getting chck letter
        btm, top = map(int, rng.split("-")) # getting the chck ranges

        part1 += btm <= pwd.count(chck) <= top # checking if the chck is within the range
        part2 += sum(pwd[x-1] == chck for x in (btm, top)) == 1  # checking if the chck only occurs once in the two certain positions in the string
        # for x in (btm, top) -> x will be btm, then top. summing will take place at the end.

    print(part1)
    print(part2)

if __name__ == "__main__":
    main()