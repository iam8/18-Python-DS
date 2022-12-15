def reverse_vowels(s):
    """
    Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    all_vowels = ["a", "e", "i", "o", "u"]

    s_chars = list(s)
    s_vowels = [char for char in s if char.lower() in all_vowels]

    for idx in range(len(s_chars)):
        if s_chars[idx].lower() in all_vowels:
            s_chars[idx] = s_vowels.pop()

    return "".join(s_chars)
