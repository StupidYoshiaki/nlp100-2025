N = 10

with open("../../data/ch02/popular-names.txt", "r") as f:
    for i, l in enumerate(f):
        if i > N-1:
            break
        print(l.replace("\t", " "), end="")
