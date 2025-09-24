import re
from commands import PREFIX
from commands import rules



def try_text(command_string): #returns a string to be sent back or None
    if command_string[0:len(PREFIX)] == PREFIX:
        return parse(command_string[len(PREFIX):], rules)

#user provides a dictionary of regexps and their behavior

def parse(command_string, rules): #returns a string to be sent back or None
    for pattern in rules:
        match = re.search(pattern, command_string)
        if match is not None:
            return rules[pattern](match.groups()) #call the function associated with the matched rule and pass the matched groups as a tuple

