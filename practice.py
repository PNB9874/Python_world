input = "a4f3g2h1"
output = ""
for ch in input:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output += d*x
print(output)