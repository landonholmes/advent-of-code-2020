
# ------------------- THE ACTUAL PROGRAM -------------------
groups = []
answer_count = 0

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]

current_group_answers = []

for line in lines:
    if line == '':
        groups.append(current_group_answers)
        current_group_answers = []
        continue

    for answer in list(line):
        if answer not in current_group_answers:
            current_group_answers.append(answer)
            answer_count += 1

# grab that last passport
groups.append(current_group_answers)


print('Sum of Yes Answer Counts:', answer_count)  # 6249