def titleize(phrase):
    """
    Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    # Forgot about str.title() method

    words = phrase.split(" ")
    words_cap = [word.capitalize() for word in words]

    return " ".join(words_cap)
