validPasswords = 0

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    for line in lines:
        pi = line.split(':')
        policy = pi[0].split(' ')

        positionalRequirements = policy[0].split('-')
        firstPos = int(positionalRequirements[0])
        secondPos = int(positionalRequirements[1])

        requiredLetter = policy[1]

        password = list(pi[1].lstrip(' '))

        doesFirstMatch = password[firstPos-1] == requiredLetter
        doesSecondMatch = password[secondPos-1] == requiredLetter

        if doesFirstMatch ^ doesSecondMatch:
            validPasswords += 1

print('Solution:', validPasswords) # 737
