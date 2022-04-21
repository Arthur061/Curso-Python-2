frase = str(input('Digite sua frase: ')).strip().upper()  # Recebeu a frase e tirou espaços e deciou tudo em MAIUSCULO

palavras = frase.split()  # Dividiu a frase
junta = ''.join(palavras)  # Juntou tudo em uma só string
inverso = ''  # Usa a opção a baixo ( for ) ou inverso = junto[::-1]

for letra in range(len(junta) -1, -1, -1):  # Criando o inverso da frase
    inverso += junta[letra]

if inverso == junta:
    print('A frase {} é um palindromo!! Resultado invertido {}'.format(frase, inverso))
else:
    print('A frase {} não é um palindromo!! ')
