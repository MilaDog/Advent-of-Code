# Day 3 - Parts 1 & 2

from sys import argv

def main():
    script, fileName = argv
    d3File = open(fileName, "r").read().splitlines()

    x_slopes = [1, 3, 5, 7, 1]
    y_slopes = [1, 1, 1, 1, 2]

    totalTrees = 1

    for x_change, y_change in zip(x_slopes, y_slopes): # tuple made. Get changes
        trees = 0
        x = 0 # initial position
        for pos in d3File[::y_change]: # getting every 'y_change' line in the list. Jumps by 'y_change' amount
            if pos[x % len(pos)] == '#': # position % length of line -> char at that point
                trees += 1
            x += x_change
        print(trees)
        totalTrees *= trees
    print(totalTrees)

main()