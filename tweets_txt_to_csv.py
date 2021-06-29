def verifica_posicoes(chave):
    chave_ordenada = sorted(chave)
    posicoes_chave = []
    for letra in chave:
        posicoes_chave.append(chave_ordenada.index(letra))

    return posicoes_chave



def cifras_transposicao(dado):
    texto = dado

    chave = 'SWITZERLAND'

    gera_posicoes_cripto = verifica_posicoes(chave)
    
    j = 0
    lista_cripto = []
    while 0 < len(texto):
        i = 0
        lista_temp = []
        while i < len(chave):
            if not texto:
                break
            lista_temp.append(texto[:1])
            texto = texto[1:]
            i += 1

        lista_cripto.append(lista_temp)

    string_codificada = ''

    for lista in lista_cripto:
        for i in range(len(chave)):
            indice = gera_posicoes_cripto.index(i)
            try:
                string_codificada += lista[indice]
            except IndexError:
                break

    return string_codificada



f = open("sort_tweets.txt", "r", encoding="UTF-8")
a = open("tweets.csv", "w", encoding="UTF-8")
a.write('tweet_id;text;user;date;location;hashtags\n')
lista_id = []
for linha in f:
    if not linha[:19].strip().upper() in lista_id:
        lista_id.append(linha[:19].strip().upper())
        a.write(
            cifras_transposicao(linha[:19].strip().upper()) + ';' +
            linha[19:299].strip().upper() + ';' +
            linha[299:319].strip().upper() + ';' +
            linha[319:327].strip().upper() + ';' +
            linha[327:377].strip().upper() + ';' +
            linha[377:577].strip().upper() + '\n'
        )