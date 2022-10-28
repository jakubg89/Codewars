"""
DESCRIPTION:
Complete the function that returns an array of length n, starting with the given number x and the squares
of the previous number. If n is negative or zero, return an empty array/list.

Examples
2, 5  -->  [2, 4, 16, 256, 65536]
3, 3  -->  [3, 9, 81]

"""


def squares(x, n):
    squares = []
    if n > 0:
        squares.append(x)
        for i in range(1, n):
            squares.append(squares[-1] ** 2)
    return squares



# best practice from Codewars
def squares2(x,n):
    return [x**(2**i) for i in range(n)]
