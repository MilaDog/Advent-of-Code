# Day 5 - Part 1 & 2

from sys import argv

def main():
    script, fileName = argv
    fin = open(fileName, "r")
    seat_codes = [line.strip() for line in fin.readlines() if line.strip()]

    total_rows = 128
    total_columns = 8
    highest_id = 0

    seat_ids = []

    for seat_code in seat_codes:
        max_row, min_row = 0, 0

        fnl_row = bsp(seat_code[:7], 128)
        fnl_col = bsp(seat_code[7:], 8)

        tot = int(fnl_row*8 + fnl_col)
        if tot > highest_id:
            highest_id = tot
        
        seat_ids.append(tot)
        
            
    print("Highest: ", highest_id)
    seat_ids.sort()

    # Couldn't do part 2


def bsp(entry, amt):
    max_pos, min_pos = 0, 0
    entry_len = len(entry)    

    plc = amt

    for ltr in entry[:entry_len-1]:
        cur = (plc/2)-1

        if ltr.lower() == "f" or ltr.lower() == "l": # lower half
            max_pos = cur + min_pos
            min_pos = min_pos

        elif ltr.lower() == "b" or ltr.lower() == "r": # upper half
            max_pos = min_pos + ((2*cur) +1)
            min_pos = min_pos + cur+1

        plc = cur + 1


    if entry[entry_len-1].lower() == "f" or ltr.lower() == "l":
        return min_pos

    elif entry[entry_len-1].lower() == "b" or ltr.lower() == "r":
        return max_pos

if __name__ == "__main__":
    main()