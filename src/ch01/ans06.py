def ngram(inputs: list[str], n: int) -> list[str|list[str]]:
    return [inputs[i:i+n] for i in range(len(inputs)-n+1)]

text1 = "paraparaparadise"
text2 = "paragraph"

X = set(ngram(text1, 2))
Y = set(ngram(text2, 2))

print(X | Y)
print(X & Y)
print(X - Y)
print("se" in (X & Y))
