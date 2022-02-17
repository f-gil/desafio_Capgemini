from string import ascii_lowercase
from string import ascii_uppercase

def verifica_senha(n): 
    carac_esp = '!@#$%^&*()-+'
    numbers = '1234567890'

    if len(n) < 6:
        return False
    
    else:
        contLower = 0
        contUpper = 0
        contNumber = 0
        contEsp = 0
        for i in range(len(n)):
            if n[i] in ascii_lowercase:
                contLower+=1
            if n[i] in ascii_uppercase:
                contUpper+=1
            if n[i] in numbers:
                contNumber+=1
            if n[i] in carac_esp:
                contEsp+=1

        if (contLower !=0 
            and contUpper != 0
            and contNumber != 0
            and contEsp !=0):
            return True
        else:
            return False


senha = str(input('Digite sua senha: '))

if verifica_senha(senha) == True:
    print(f'Senha cadastrada com sucesso!')
else: 
    print(f'Sua senha deve contar pelo menos 6 caráctéres, tem {len(senha)}')
    if len(senha) < 6:
        print(f'Faltam {6 - len(senha)} caractéres.')

    print()
    print('Lembrando que são:')
    print('no mínimo 1 digito')
    print('no mínimo 1 letra em minúsculo.')
    print('no mínimo 1 letra em maiúsculo.')
    print('no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+')
