N = 10

with open("../../data/ch02/popular-names.txt", "r") as f:
    names = f.readlines()
print("".join(names[-N:]))
