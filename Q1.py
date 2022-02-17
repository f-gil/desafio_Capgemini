n = int(input('Digiter o valor de n: '))

vet = [' '] * n
cont = 0

for i in range (n):
    cont -= 1
    vet[cont] = '*'
    for j in range(n):
        print(vet[j], end='')
    print()
        
