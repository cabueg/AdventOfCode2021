def part1():
    f = open('./inputs/day1.txt', 'r')

    lines = f.readlines()
    amt = 0
    ans = []
    for line in lines:
        if line == '\n':
            ans.append(amt)
            amt = 0
        else:
            amt += int(line)
    f.close()
    return max(ans)

def part2():
    f = open('./inputs/day1.txt', 'r')
    lines = f.readlines()
    amt = 0
    total = 0
    ans = []


    for line in lines:
        if line == '\n':
            ans.append(amt)
            amt = 0
        else:
            amt += int(line)


    for _ in range(3):
        temp = max(ans)
        ans.remove(temp)
        total += temp
    return total

print(part2())