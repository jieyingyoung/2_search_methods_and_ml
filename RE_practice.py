import re

example_sentence = "guru99 get , guru99 give , guru Selenium"

# re.findall()

# Example of w+ and ^ Expression
# "^": This expression matches the start of a string
# "w+": This expression matches the alphanumeric character in the string
starter = re.findall(r"^\w+",example_sentence)
print('Example of w+ and ^ Expression', starter)

# Example of \s expression in re.split function
spliter = re.split(r'\s', example_sentence)
print('Example of \s expression in re.split function', spliter)

# Example of 's' expression in re.split function
spliter = re.split(r'\s', example_sentence)
print('Example of \s expression in re.split function', spliter)

# re.
list = [example_sentence]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
    if z:
        print((z.groups()))