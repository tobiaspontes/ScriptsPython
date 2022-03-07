def is_isogram(string):
    ''' Esta função retorna verdadeiro se uma palavra for isograma '''
    ''' Isograma é quando uma palavra não tem nenhuma letra repetida '''
    letter_list = []
    for letter in string:
        if letter != ' ' and letter != '-':
            for item in letter_list:
                if letter.upper() == item.upper():
                    return False
            letter_list.append(letter)

    return True
