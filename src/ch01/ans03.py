import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

text = re.sub("[,|.]", "", text)
words = [len(word) for word in text.split()]
print(words)
