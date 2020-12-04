# Day 4 - Part 1 & 2

from sys import argv

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def main():
    script, inputFile = argv
    fin = open(inputFile, "r")

    lines = fin.read().split("\n\n")
    lines = [line.strip() for line in lines if line.strip()]

    valid = 0
    tot_valid = 0
    count = 0
    for line in lines:
        parts = line.split("\n")

        fields_all = []
        fields_all_2 = []
        for part in parts:
            part = part.strip()
            fields = part.split(" ")

            for field in fields:
                fields_all.append(field[:3])
                fields_all_2.append(field)
                if field[:3] in valid_fields:
                    count += 1
        
        if count == 8:
            valid += 1

            if validation(fields_all_2):
                tot_valid += 1 

        elif count == 7 and "cid" not in fields_all:
            valid += 1

            if validation(fields_all_2):
                tot_valid += 1 


        count = 0
    print(valid)
    print(tot_valid)

def validation(passport):
    valid = True
    # print(passport)
    for x in passport:
        field, value = x.split(":")
        # print(field, value)

        if field == 'byr':
            if not 1920 <= int(value) <= 2002:
                # print("Invalid field")
                valid = False
            elif len(value) != 4:
                # print("Invalid field")
                valid = False

        elif field == 'iyr':
            if not 2010 <= int(value) <= 2020:
                # print("Invalid field")
                valid = False
            elif len(value) != 4:
                # print("Invalid field")
                valid = False

        elif field == 'eyr':
            if not 2020 <= int(value) <= 2030:
                # print("Invalid field")
                valid = False
            elif len(value) != 4:
                # print("Invalid field")
                valid = False
        
        elif field == 'hgt':
            if value.endswith("cm"):
                if not 150 <= int(value.replace("cm", "")) <= 193:
                    # print("Invalid field")
                    valid = False
            elif value.endswith("in"):
                if not 59 <= int(value.replace("in", "")) <= 76:
                    # print("Invalid field")
                    valid = False
            else:
                valid = False
        
        elif  field == 'hcl':
            if value.startswith("#"):
                if len(value[1:]) != 6:
                    # print("Invalid field")
                    valid = False
                else:
                    for n in value.replace("#", ""):
                        if n not in ['a', 'b', 'c', 'd', 'e', 'f', '1', '0', '2', '3', '4', '5', '6', '7', '8', '9']:
                            # print("Invalid field")
                            valid = False
            else:
                # print("INvalid")
                valid = False

        elif field == 'ecl':
            if value.lower() not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                # print("Invalid field")
                valid = False

        elif field == 'pid':
            if len(value) != 9:
                # print("Invalid field")
                valid = False

        elif field == 'cid':
            if len(passport) < 7:
                valid = False

    if valid == True:
        return True 

if __name__ == "__main__":
    main()