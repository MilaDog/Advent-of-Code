# Day 2 - Parts 1 & 2

from sys import argv

def main():
    script, fileName = argv
    d2File = open(fileName, "r").read().splitlines()

    print(part1(d2File)) # 614
    print(part2(d2File)) # 354

def part1(lines):
    totalCorrectPwd = 0
    for line in range(len(lines)):
        pwdRange, ltr, pwd = lines[line].split(" ") # spliting line into the parts that need to be used
        pwdRange1, pwdRange2 = pwdRange.split("-") # spliting password range
        ltr = ltr.replace(":", "") # getting just the letter to be used
        
        count = 0
        for char in pwd: # looping through password
            if str(char) == str(ltr): # checking if each char is equal to the check letter
                count += 1

        if int(pwdRange1) <= count <= int(pwdRange2): # checking iof the number of check letters in the password is in the specified range
            totalCorrectPwd += 1         

    return totalCorrectPwd

def part2(lines):    
    totalCorrectPwd = 0
    for line in range(len(lines)):
        pwdRange, ltr, pwd = lines[line].split(" ") # spliting line into the parts that need to be used
        pwdRange1, pwdRange2 = pwdRange.split("-") # spliting password range
        ltr = ltr.replace(":", "") # getting just the letter to be used

        # checking if the check letter only appears once in the certain positions in the password. False if it is occuring in both places
        if pwd[int(pwdRange1)-1] == ltr and pwd[int(pwdRange2)-1] != ltr:
            totalCorrectPwd += 1
        elif pwd[int(pwdRange1)-1] != ltr and pwd[int(pwdRange2)-1] == ltr:
            totalCorrectPwd += 1

    return totalCorrectPwd

main()