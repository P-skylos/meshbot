import re


PREFIX = '!'

#user provides a dictionary of regexps and their behavior

def parse(command_string, rules):
    for pattern in rules:
        match = re.search(pattern, command_string)
        if match is not None:
            return rules[pattern](match.groups()) #call the function associated with the matched rule and pass the matched groups as a tuple

