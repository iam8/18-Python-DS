def sum_up_diagonals(matrix):
    """
    Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # TL-BR, any square matrix: (0, 0), (1, 1), (2, 2)...
    # BR-TL, 3x3 matrix: (0, 2), (1, 1), (2, 0)
    # BR-TL, nxn matrix: (0, n-1), (1, n-2), (2, n-3), (3, n-4) ... (n-2, 1), (n-1, 0)

    sum_TL_BR = 0
    sum_BR_TL = 0

    for rownum in range(len(matrix)):
        for colnum in range(len(matrix)):
            if rownum == colnum:
                sum_TL_BR += matrix[rownum][colnum]

            if rownum + colnum == len(matrix) - 1:
                sum_BR_TL += matrix[rownum][colnum]

    return sum_TL_BR + sum_BR_TL
