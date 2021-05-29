T = int(input())
for t in range(T):
    linha = input().split(' ')
    x = float(linha[0])
    y = float(linha[1])
    somatorio = x + y
    if somatorio <= float(linha[2]):
        print("CABE!", end="" if t == T - 1 else "\n")
    else:
       print("NAO CABE!", end="" if t == T - 1 else "\n") 