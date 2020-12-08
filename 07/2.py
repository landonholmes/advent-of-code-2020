import re


def parse_bag_rules():
    rules_parsed = {}
    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines:
        bag_rules_split = line.split(' bags contain')
        outer_bag = bag_rules_split[0]
        inner_bags = bag_rules_split[1].strip()
        rules_parsed[outer_bag] = re.findall(r'([0-9]+) ([a-z ]+) bag[s]?', inner_bags)

    return rules_parsed


def count_inner_bags_for_color(bag_rules, bag_color):
    def search_for_bag(current_bag):
        return sum(int(count) + int(count) * search_for_bag(bag) for count, bag in bag_rules[current_bag])

    return search_for_bag(bag_color)


rules = parse_bag_rules()
bag_colors_required_within_shiny_gold = count_inner_bags_for_color(rules, 'shiny gold')

print('Kinds of bags required within shiny gold bag: ', bag_colors_required_within_shiny_gold)

