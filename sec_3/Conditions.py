# if / elif / else
a = 33; b = 200
if b > a:
    print("b أكبر من a")     # ← هيطبع ده
elif a == b:
    print("متساويين")
else:
    print("a أكبر")

# Short hand (ternary)
print("A") if a > b else print("B")