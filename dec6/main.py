import re
from functools import reduce
from itertools import chain

with open('problem_data.txt') as file:
    full_text = file.read()
    groups_as_string = re.sub("\\n(?!\\n)", "", full_text).split("\n")
    group_answers = map(set, groups_as_string)
    total_unique_answers = len(list(chain(*list(group_answers))))
    print(f"Sum of group answers: {total_unique_answers}")

    groups = [map(set, group.split("\n")) for group in full_text.split("\n\n")]
    shared_values = [reduce(set.intersection, group) for group in groups]
    total_shared_answers = total_unique_answers = len(list(chain(*list(shared_values))))
    print(f"Answer problem 2 is: {total_shared_answers}")