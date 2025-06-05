text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

atomic = {}
cnt = 0
for word in text.split():
    cnt += 1
    if cnt in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        atomic[word[0]] = cnt
    else:
        atomic[word[:2]] = cnt

print(atomic) 
