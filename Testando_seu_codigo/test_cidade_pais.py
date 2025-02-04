import cidade_pais

def test_cidade_pais():
    """importando o modulo e a função"""
    endereco = cidade_pais.cidade_pais('São Paulo','SP')
    assert endereco == "São Paulo, SP"

