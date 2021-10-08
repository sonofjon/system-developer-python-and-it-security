""" You are provided with the following phrase:

phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'

Use python lib re and try to find:

Sequence of digits
Sequence of non-digits
Sequence of whitespace
Sequence of non-whitespace
alphanumeric characters
non alphanumeric """

import re

phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'

# Sequence of digits
matches = re.findall("\d+", phrase)
print("digits:", matches)

# Sequence of non-digits
matches = re.findall("\D+", phrase)
print("non-digits:", matches)

# Sequence of whitespace
matches = re.findall("\s+", phrase)
print("whitespace:", matches)

# Sequence of non-whitespace
matches = re.findall("\S+", phrase)
print("non-whitespace:", matches)

# alphanumeric characters
matches = re.findall("[a-zA-Z0-9]+", phrase)
print("alphanumeric:", matches)

# non alphanumeric
matches = re.findall("[^a-zA-Z0-9]+", phrase)
print("non-alphanumeric:", matches)
