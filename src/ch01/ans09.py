import random
from collections.abc import Generator

def typoglycemia(words: list[str]) -> Generator:
    for word in words:
        if len(word) <= 4:
            yield word
        else:
            target = word[1:-1]
            yield word[0] + "".join(random.sample(target, len(target))) + word[-1]

text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

gen = typoglycemia(text.split())
print(" ".join(gen))
