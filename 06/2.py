groups = []
answer_count = 0

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]

current_group_answers = {
    'answers': [],
    'number_in_group': 0
}

for line in lines:
    if line == '':
        groups.append(current_group_answers)
        current_group_answers = {
            'answers': [],
            'number_in_group': 0
        }
        continue

    for answer in list(line):
        current_group_answers['answers'].append(answer)

    current_group_answers['number_in_group'] += 1

# grab that last passport
groups.append(current_group_answers)

for group in groups:
    unique_answers = set(group['answers'])
    for answer in unique_answers:
        # check if the answers we found were said yes in each group for the amount of group members
        if group['answers'].count(answer) == group['number_in_group']:
            answer_count += 1


print('Sum of Yes Answer Counts:', answer_count)  #
