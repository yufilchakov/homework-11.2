def uppercase_string(input_string):
    return input_string.upper()


def capitalize_words(input_string):
    """
    Функция принимает на вход строку и возвращает ее со всеми заглавными буквами.
    """
    return ' '.join(word.capitalize() for word in input_string.split())
