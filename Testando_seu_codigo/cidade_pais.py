

def cidade_pais(cidade, pais, populacao = ''):
    if populacao:
        endereco_completo = f"{cidade}, {pais}, {populacao}"
    else:
        endereco_completo = f"{cidade}, {pais}"
    return endereco_completo


