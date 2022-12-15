def same_frequency(num1, num2):
    """
    Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_str = str(num1)
    num2_str = str(num2)

    # Make digit frequency dicts for each num
    freqs_1 = {digit : num1_str.count(digit) for digit in num1_str}
    freqs_2 = {digit : num2_str.count(digit) for digit in num2_str}

    return freqs_1 == freqs_2
