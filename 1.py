kolvo=input("Введите количество слов")
i=0
s=""
while i<int(kolvo):
    s1=input()
    s=s+s1+" "
    i=i+1
s_new=s[:-1]
print(s_new)
