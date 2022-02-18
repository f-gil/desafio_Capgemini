string = str(input('digita: '))

vetor_strings = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]

def hashtable(vetor):
    anagramas = {}
    for palavra in vetor:
        palavra_ordenada = "".join(sorted(palavra))
        if palavra_ordenada in anagramas:
            anagramas[palavra_ordenada].append(palavra)    
        else:
            anagramas[palavra_ordenada] = [palavra]
    return list(anagramas.values())


vetor_aux = hashtable(vetor_strings)

pares_anagramas = []
for k in range(len(vetor_aux)):
    if len(vetor_aux[k]) > 1:
        pares_anagramas.append(vetor_aux[k])
        

print(pares_anagramas)
print(len(pares_anagramas))
