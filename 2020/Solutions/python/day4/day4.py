# Day 4 - Part 1 & 2

from sys import argv

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def main():
    script, inputFile = argv
    fin = open(inputFile, "r")

    spp = fin.read().split("\n\n") # getting a single passport
    opp = [t.replace("\n", " ") for t in spp] # one passport per index as one string with whitespace between field:value

    part1(opp)


def part1(passports):
    valid_passport = 0
    tot_valid = 0
    for pp in passports:
        fields = pp.split(" ")

        field_values = map(lambda x: x[:3], fields) # mapping to only contain field key

        # Length checking
        if len(fields) == 8:
            valid_passport += 1

            # Going to part2 for validation
            if part2(fields) == True:
                tot_valid += 1

        elif len(fields) == 7 and 'cid' not in list(field_values):
            valid_passport += 1

            # Going to part2 for validation
            if part2(fields) == True:
                tot_valid += 1

    print(valid_passport)
    print(tot_valid)


def part2(passport):
    parts = map(lambda x: x.split(":"), passport) # getting list of parts -> [ [field_key, value], [field_key, value]... ]

    # Checking
    valid = True
    for part in list(parts):
        if part[0] == 'byr':
            if val_byr(part[1]) == False:
                valid = False
        elif part[0] == 'iyr':
            if val_iyr(part[1]) == False:
                valid = False
        elif part[0] == 'eyr':
            if val_eyr(part[1]) == False:
                valid = False
        elif part[0] == 'hgt':
            if val_hgt(part[1]) == False:
                valid = False
        elif part[0] == 'hcl':
            if val_hcl(part[1]) == False:
                valid = False
        elif part[0] == 'ecl':
            if val_ecl(part[1]) == False:
                valid = False
        elif part[0] == 'pid':
            if val_pid(part[1]) == False:
                valid = False
        elif part[0] == 'cid':
            if val_cid(passport) == False:
                valid = False
        
    if valid == True:
        return True


def val_byr(value):
    if len(value) == 4:
        if not 1920 <= int(value) <= 2002:
            return False
    else:
        return False
        

def val_iyr(value):
    if len(value) == 4:
        if not 2010 <= int(value) <= 2020:
            return False
    else:
        return False


def val_eyr(value):
    if len(value) == 4:
        if not 2020 <= int(value) <= 2030:
            return False
    else:
        return False


def val_hgt(value):
    if value.lower().endswith("cm"):
        if not 150 <= int(value[:len(value)-2]) <= 193:
            return False
    elif value.lower().endswith("in"):
        if not 59 <= int(value[:len(value)-2]) <= 76:
            return False
    else:
        return False


def val_hcl(value):
    valid_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
    if value.startswith("#"):
        if len(value[1:]) == 6:
            if not (lambda x: x in valid_characters, value[1:]):
                return False
        else:
            return False
    else:
        return False


def val_ecl(value):
    valid_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value not in valid_colours:
        return False


def val_pid(value):
    if len(value) != 9:
        return False


def val_cid(value):
    if len(value) < 7:
        return False 


if __name__ == "__main__":
    main()