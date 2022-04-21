lista_nome = []  # Criando lista para nomes
lista_nome_homem = []  # Criando lista para homem mais velho
lista_idade = []  # Lista para somar idades
lista_sexo = []  # Lista dos sexos das pessoas
lista_idade_homem = []  # Lista para maior idade dos homens
lista_idade_mulher = []  # Lista para idade de mulher com menos de 20 anos

for c in range(1, 5):
    print('     {}ª pessoa     '.format(c))
    nome = str(input('Digite o nome: ')).strip().upper()
    lista_nome.append(nome)  # Adiciona os nomes na lista

    idade = int(input('Digite a idade: '))
    lista_idade.append(idade)  # Adiciona idades na lista

    sexo = str(input('Digite o sexo (M / F): ')).strip().upper()
    lista_sexo.append(sexo)  # Adiciona os sexos na lista

    if sexo == 'M':
        lista_nome_homem.append(nome)  # Adicionando todos homens na lista
        lista_idade_homem.append(idade)  # Adicionando todas as idades dos homens na lista

    if sexo == 'F' and idade < 20:
        lista_idade_mulher.append(idade)  # Adicionando as idades das mulheres na lista

# Função sun(soma todas as idades) / e len(ler cada idade)

print('A média de idade do grupo é {}'.format(sum(lista_idade)/len(lista_idade)))

# Função index(retorna a posição em que o item se encontra dentro da lista) / max(define qual maior idade)

print('Nome do homem mais velho: {}'.format(lista_nome_homem[lista_idade_homem.index(max(lista_idade_homem))]))

# Função len(ler a idade das mulher e define qual a menor)

print('O total de mulheres abaixo de 20 anos: {}'.format(len(lista_idade_mulher)))