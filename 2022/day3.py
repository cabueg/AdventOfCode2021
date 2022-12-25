from curses.ascii import isupper


def getRepeat(firstHalf, secondHalf):
    for c in firstHalf:
        if c in secondHalf:
            return c



def part1():
    f = open('inputs/day3.txt', 'r')
    lines = f.readlines()
    ans = 0

    for line in lines:
        half = int((len(line)-1)/2)
        firstHalf = line[:half]
        secondHalf = line[half:]
        buh = getRepeat(firstHalf, secondHalf)
        if isupper(buh): ans += (ord(buh) - ord('A')) + 27
        else: ans += (ord(buh) - ord('a')) + 1

    return ans


#print(f'Part 1 Ans: {part1()}')


def part2():
    ans = 0
    with open('./inputs/day3.txt') as f:
        while f:
            line1 = f.readline()
            line2 = f.readline()
            line3 = f.readline()
            print(line1, line2, line3)

	#return


print(f'Part 2 Ans: {part2()}')


