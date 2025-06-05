def ngram(inputs: list[str], n: int) -> list[str|list[str]]:
    outputs = []
    for i in range(len(inputs)-n+1):
        outputs.append(inputs[i:i+n])
    return outputs

text = "I am an NLPer"
print(ngram(text, 3))
print(ngram(text.split(), 2))
