passports = []
validFound = 0
requiredFields = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    # 'cid',  # (Country ID)
]


def validate_passport(pp):
    for field in requiredFields:
        if field not in pp:
            return False
    return True


with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]

currentPassport = {}

for line in lines:
    if line == '':
        passports.append(currentPassport)
        currentPassport = {}
        continue

    if line.count(' ') > 0:
        splitLine = line.split(' ')
        for group in splitLine:
            [key, value] = group.split(':')
            currentPassport[key] = value
    else:
        [key, value] = line.split(':')
        currentPassport[key] = value

# grab that last passport
passports.append(currentPassport)

for passport in passports:
    validFound += 1 if validate_passport(passport) else 0

print('Valid:', validFound)  # 208
