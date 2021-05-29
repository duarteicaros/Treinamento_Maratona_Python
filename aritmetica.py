x = int(input())
s1 = input()
y = int(input())
s2 = input()
z = int(input())

if s1 == '*':
    conta = x * y
    if s2 == '+':
        conta = conta + z
        print(int(conta), end="")
    elif s2 == '-':
        conta = conta - z
        print(int(conta), end="")
elif s1 == '/':
    if y == 0:
        print("erro", end="")
    else:
        conta = x / y
        if s2 == '+':
            conta = conta + z
            print(int(conta), end="")
        elif s2 == '-':
            conta = conta - z
            print(int(conta), end="")
elif s2 == '*':
    conta = y * z
    if s1 == '+':
        conta = x + conta
        print(int(conta), end="")
    elif s1 == '-':
        conta = x - conta
        print(int(conta), end="")
elif s2 == '/':
    if z == 0:
        print("erro", end="")
    else:
        conta = y / z
        if s1 == '+':
            conta = x + conta
            print(int(conta), end="")
        elif s1 == '-':
            conta = x - conta
            print(int(conta), end="")
elif s1 == '+':
    conta = x + y
    if s2 == '*':
        conta = conta * z
    elif s2 == '/':
        if z == 0:
            print("erro", end="")
        else:
            conta = conta / z
            print(int(conta), end="")
    elif s2 == '+':
            conta = conta + z
            print(int(conta), end="")
    elif s2 == '-':
            conta = conta - z
            print(int(conta), end="")
elif s1 == '-':
    conta = x - y
    if s2 == '*':
        conta = conta * z
        print(int(conta), end="")
    elif s2 == '/':
        if z == 0:
            print("erro", end="")
        else:
            conta = conta / z
            print(int(conta), end="")
    elif s2 == '+':
            conta = conta + z
            print(int(conta), end="")
    elif s2 == '-':
            conta = conta - z
            print(int(conta), end="")