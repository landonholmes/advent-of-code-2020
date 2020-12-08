from collections import defaultdict
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


def count_outer_bags_for_color(bag_rules, bag_color):
    # this will let us not check if it already exists in dict. if not found, it gets created
    inverted_bag_rules = defaultdict(list)

    for outer_bag, inner_bags in bag_rules.items():
        for count, bag in inner_bags:
            inverted_bag_rules[bag].append(outer_bag)

    def search_for_bag(target_bag):
        seen = set()
        stack = [target_bag]
        while len(stack):
            current_bag = stack.pop()
            for parent_bag in inverted_bag_rules[current_bag]:
                if parent_bag not in seen:
                    seen.add(parent_bag)
                    stack.append(parent_bag)
        return len(seen)

    return search_for_bag(bag_color)


rules = parse_bag_rules()
bag_colors_that_can_contain_gold = count_outer_bags_for_color(rules, 'shiny gold')

print('Bag colors that can eventually contain gold: ', bag_colors_that_can_contain_gold)

