s=""
print("Вводите слова")
while True:
    s1=input()
    if s1=="stop":
        break
    else:
        s=s+s1+" "
s_new = s[:-1]
print(s_new)