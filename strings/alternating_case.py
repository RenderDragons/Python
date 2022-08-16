def alternating_case(words: str) -> str:
    """
    Returns a string with each letter alternating between lower and uppercase.
    >>> alternating_case('Hello World')
    HeLlO WoRlD
    >>> alternating_case('123585')
    123585
    >>> alternating_case('6az.*65@5')
    6aZ.*65@5
    """
    first_letter_case = False #False means the first letter is lowercase
    processed_word = ''
    if words[0].islower() and words[0].isalpha:
        first_letter_case = False
    else:
        first_letter_case = True
    for index in range(len(words)):
        if first_letter_case == True:
            processed_word += words[index].upper()
        else:
            processed_word += words[index].lower()
        first_letter_case = not first_letter_case
    return processed_word