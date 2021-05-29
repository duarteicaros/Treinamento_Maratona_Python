T = int(input())
for t in range(T):
    linha = input().split(" ")
    maximo = max([int(e) for e in linha])
    minimo = min([int(e) for e in linha])
    print(str(minimo) + ' ' + str(maximo), end="\n")
    if minimo == maximo:
        print('S', end="" if t == T - 1 else "\n")
    else:
        print('N', end="" if t == T - 1 else "\n")
