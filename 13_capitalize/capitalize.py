def capitalize(phrase):
    """
    Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    # Note: I did it the way I did below because the str.capitalize() method will also lower-case
    # any chars later in the string, messing up other capitalization; for example:
    # "party in the USA".capitalize() returns "Party in the usa"

    if not phrase:
        return ""

    words = phrase.split(" ")
    words[0] = words[0].capitalize()

    return " ".join(words)
