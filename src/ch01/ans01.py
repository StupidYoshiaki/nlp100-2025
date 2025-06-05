text = "パタトクカシーー"

ans = ""
for i in range(len(text)):
    if (i + 1) % 2 == 0:
        ans += text[i]

print(ans)
