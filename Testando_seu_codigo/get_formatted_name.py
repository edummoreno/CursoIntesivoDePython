import pytest


def get_formatted_name(first, last, middle=''):
    """gera um nome completo, elegantemente formatado"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def test_disrt_last_middle_name():
    """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amedeus Mozart'


