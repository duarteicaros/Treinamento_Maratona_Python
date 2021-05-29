v=int(input())

n100 = v // 100
print(str(n100) + " nota(s) de R$ 100")

n100res = v % 100
n50 = n100res // 50
print(str(n50) + " nota(s) de R$ 50")

n50res = n100res % 50
n20 = n50res // 20
print(str(n20) + " nota(s) de R$ 20")

n20res = n50res % 20
n10 = n20res // 10
print(str(n10) + " nota(s) de R$ 10")

n10res = n20res % 10
n5 = n10res // 5
print(str(n5) + " nota(s) de R$ 5")

n5res = n10res % 5
n2 = n5res // 2
print(str(n2) + " nota(s) de R$ 2")

n2res = n5res % 2
n1 = n2res // 1
print(str(n1) + " nota(s) de R$ 1", end='')