def rps(my_input: str, opponent_input: str) -> int:
    if my_input == opponent_input:
        return 3
    elif (my_input == 'rock' and opponent_input == 'scissors') or (my_input == 'paper' and opponent_input == 'rock') or (my_input == 'scissors' and opponent_input == 'paper'):
        return 6
    else: return 0

def rps2(opponent_input, outcome) -> int:
    if (opponent_input == 'rock' and outcome == 'tie') or (opponent_input == 'paper' and outcome == 'lose') or (opponent_input == 'scissors' and outcome == 'win'):
        return 1
    elif (opponent_input == 'rock' and outcome == 'win') or (opponent_input == 'paper' and outcome == 'tie') or (opponent_input == 'scissors' and outcome == 'lose'):
        return 2
    else: return 3

rpsMap = {
    'A': 'rock',
    'X': 'rock',
    'B': 'paper',
    'Y': 'paper',
    'C': 'scissors',
    'Z': 'scissors'
}

outcomes = {
    'X': 'lose',
    'Y': 'tie',
    'Z': 'win'
}


def part1() -> int:
    f = open('./inputs/day2.txt', 'r')
    ans = 0
    lines = f.readlines()
    for line in lines:
        opponent = rpsMap[line[0]]
        mine = rpsMap[line[2]]
        if mine == 'rock':
            ans += 1
        elif mine == 'paper':
            ans += 2
        elif mine == 'scissors':
            ans += 3
        ans += rps(mine, opponent)


    return ans# some score

def part2():
    f = open('./inputs/day2.txt', 'r')
    ans = 0
    lines = f.readlines()

    for line in lines:
        opponent = rpsMap[line[0]]
        outcome = outcomes[line[2]]
        if outcome == 'win':
            ans += 6
        elif outcome == 'tie':
            ans += 3
        elif outcome == 'lose':
            ans += 0
        ans += rps2(opponent_input=opponent, outcome=outcome)
    return ans

print(f'Part 1 answer: {part1()}')
print(f'Part 2 answer: {part2()}')