text1 = "パトカー"
text2 = "タクシー"
ans = ""

for word1, word2 in zip(text1, text2):
    ans += word1 + word2

print(ans)
