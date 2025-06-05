from collections.abc import Generator

def cipher(text: str) -> Generator:
    for char in text:
        if char.islower():
            yield chr(219 - ord(char))
        else:
            yield char

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
gen = cipher(text)

print("".join(gen))
