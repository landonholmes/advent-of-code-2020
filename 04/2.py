import re  # screeeeeeching

validFound = 0
requiredFields = [
    {
        'name': 'byr',  # (Birth Year)
        'required': True,
        'validationFunction': 'validate_birth_year'
    },
    {
        'name': 'iyr',  # (Issue Year)
        'required': True,
        'validationFunction': 'validate_issue_year'
    },
    {
        'name': 'eyr',  # (Expiration Year)
        'required': True,
        'validationFunction': 'validate_expiration_year'
    },
    {
        'name': 'hgt',  # (Height)
        'required': True,
        'validationFunction': 'validate_height'
    },
    {
        'name': 'hcl',  # (Hair Color)
        'required': True,
        'validationFunction': 'validate_hair_color'
    },
    {
        'name': 'ecl',  # (Eye Color)
        'required': True,
        'validationFunction': 'validate_eye_color'
    },
    {
        'name': 'pid',  # (Passport ID)
        'required': True,
        'validationFunction': 'validate_passport_id'
    },
    {
        'name': 'cid',  # (Country ID)
        'required': False,
        # no validation on purpose
    }
]
hairColorRegex = re.compile('^#(?:[0-9a-fA-F]{6})$')


def validate_passport(pp):
    for field in requiredFields:
        if field['required']:
            if field['name'] not in pp:  # make sure the passport has the field if it is required
                return False
            else:
                if 'validationFunction' in field:  # if we have validation to run
                    val = pp[field['name']]  # get the value from passport
                    func = globals()[field['validationFunction']]  # get validation function
                    validity = func(val)
                    if not validity:
                        return False
    return True  # we passed all the checks above


def validate_generic_year(val, minimum, maximum):
    return len(val) == 4 and minimum <= int(val) <= maximum


def validate_birth_year(val):
    return validate_generic_year(val, 1920, 2002)


def validate_issue_year(val):
    return validate_generic_year(val, 2010, 2020)


def validate_expiration_year(val):
    return validate_generic_year(val, 2020, 2030)


def validate_height(val):
    if val.count('cm') > 0:
        return 150 <= int(val.replace('cm', '')) <= 193
    elif val.count('in') > 0:
        return 59 <= int(val.replace('in', '')) <= 76
    else:
        return False


# https://stackoverflow.com/a/1636354/7800124
def validate_hair_color(val):
    return bool(hairColorRegex.match(val))  # first character is # followed by 6 characters either 0-9 or a-f


def validate_eye_color(val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_passport_id(val):
    return len(val) == 9 and val.isdigit()


def build_passports():
    passportsTemp = []

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    currentPassport = {}

    for line in lines:
        if line == '':
            passportsTemp.append(currentPassport)
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
    passportsTemp.append(currentPassport)
    return passportsTemp


passports = build_passports()

for passport in passports:
    validFound += 1 if validate_passport(passport) else 0

print('Valid:', validFound)  # 167
