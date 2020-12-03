validPasswords = 0

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    for line in lines:
        pi = line.split(':')
        policy = pi[0].split(' ')

        numberRequirements = policy[0].split('-')
        minimum = int(numberRequirements[0])
        maximum = int(numberRequirements[1])
        requiredLetter = policy[1]

        password = pi[1].lstrip(' ')

        letterCount = password.count(requiredLetter)

        if minimum <= letterCount <= maximum:
            validPasswords += 1

print('Solution:', validPasswords) # 645
