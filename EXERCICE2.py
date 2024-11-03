U1 = []
L = []
U2 = [0, 0, 0]
for i in range(3):
    n = int(input("veuillez entrez un nombre : "))
    U1.append(n)
for i in range(3):
    while True:
        x = int(input("veuillez entrez une valeur (0 ou 1 seulement) : "))
        if x == 0 or x == 1:
            L.append(x)
            break
for i in range(3):
    if L[i] == 1:
        U2[i] = U1[i]
    elif L[i] == 0 and i < 2:
        U2[i] = U1[i + 1]
        break

print("U1 :", U1)
print("L :", L)
print("U2 :", U2)
