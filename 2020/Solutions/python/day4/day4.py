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
        
    if valid == True:
        return True


def range_check(min, max, value):
    return min <= value <= max

def val_byr(value):
    if len(value) == 4:
        if not range_check(1920, 2002, int(value)):
            return False
    else:
        return False
        

def val_iyr(value):
    if len(value) == 4:
        if not range_check(2010, 2020, int(value)):
            return False
    else:
        return False


def val_eyr(value):
    if len(value) == 4:
        if not range_check(2020, 2030, int(value)):
            return False
    else:
        return False


def val_hgt(value):
    if value.lower().endswith("cm"):
        if not range_check(150, 193, int(value[:len(value)-2])):
            return False
    elif value.lower().endswith("in"):
        if not range_check(59, 76, int(value[:len(value)-2])):
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
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def val_pid(value):
    if len(value) != 9:
        return False
    else:
        try:
            int(value)
        except Exception:
            return False


if __name__ == "__main__":
    main()