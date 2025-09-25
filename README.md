# vision
This is a small python script that filters incoming messages for ones with a command prefix, interprets those commands, and then sends the required response. For example it might receive the message `!temp 2000` and send back `the local forecast is a high of 65 fahrenheit for 20:00`.

# status
This bot is in its proof of concept stage. Once error handling is added I would consider it a minimum viable product. After that, it's refining usability.

# Structure
`bot.py` contains the connection and bot logic 
`command_parse.py` contains the parsing logic
`commands.py` is intended to be edited by the end user. It should contain a variable called `PREFIX` which specifies what all bot commands should be prefixed with in order for the bot to respond to them, (this is the "!" in our vision example) and it should have a dictionary called `commands` where each key is a regular expression with a capture group for each command argument and each corresponding value is a function that will be given a tuple of the matched capture groups and will return the desired response.

# configuring the bot
All configuration is done in the `commands.py` file. Set the command prefix by assigning a string to `PREFIX` and set commands by giving a pattern and function in the `commands` dict. These two items are imported into the parser explicitly by name so keep their names the same. Nothing else will be imported. If you look in the commands file right now you can see some example default commands. Below is another illustrative example:

```Python
PREFIX = "!"
def calculator(tuple):
	a, op, b = tuple
	ops = {
        "+": (lambda x,y: x+y),
        "-": (lambda x,y: x-y),
        "/": (lambda x,y: x/y),
        "*": (lambda x,y: x*y)
    }
    return str(ops[op](int(a), int(b)))
	
commands = {
	"calc ([0-9]+)([+/*\-])(0-9)":calculator
}
```

say our bot now sees the message `!calc 500+7` it will first recognize the prefix `!`, then pass on the rest of the message to the regex checker, which will match our rule and extract our three capture groups (the parts of the pattern in parentheticals). Then it calls our `calculator` function with an argument of `("500", "+", "7")` which our calculator function now has to unpack and process into a response that MUST be a string.

To learn more about python regex and capture groups, you can start [here](https://www.programiz.com/python-programming/regex) and [here](https://pynative.com/python-regex-capturing-groups/)

note that when matching groups, only the last matched substring is recorded. for this reason its not recommended to use repeating capture groups.


# To-do's.
- we need to make sure the bot responds on the same channel it was messaged on
- do we want to pass on metadata also?
- add guidance to commands.py
- add common issues to the how to use section
- add testing
- add error handling


