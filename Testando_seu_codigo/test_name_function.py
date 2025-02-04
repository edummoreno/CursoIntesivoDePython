from get_formatted_name import get_formatted_name


def test_first_last_name():
    """"Nomes como 'janis joplin' funcionam?"""
    formatted_name = get_formatted_name('janis','joplin')
    #whatis assert?
    assert formatted_name == 'Janis Joplin'