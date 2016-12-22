'''
O(n*m) time complexity
O(n*m) space complexity
Given the height and width of a minesweeper board
and the number of bombs, return a board that has those
bombs evenly distributed
'''
import random
def minesweeper(m, n, x):
    board = [[0 for _ in xrange(n)] for _ in xrange(m)]
    spaces_left = m*n
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            if x != 0:
                if random.randint(0, int(spaces_left/x)) == 0:
                    board[i][j] = 1
                    x -= 1
                spaces_left -= 1
    return board


'''
O(logn) time complexity
O(1) space complexity
returns the number of trailing zeroes
in n factorial
'''
def count_trailing_zeros_in_fact(n):
    count = 0
    i = 5
    while n / i != 0:
        count += n / i
        i *= 5
    return count


'''
O(1) time complexity
O(1) space complexity since a 64 bit int can only have 20 digits
Given a number find the next number that is a palindome,
For example if given 10 you should return 11 since 11 is the first
palindome after 10, if given 19 you should return 22 for the same reason.
'''
import math
def next_palindome(n):
    s = str(n)
    left = s[:len(s)/2]
    right = s[int(math.ceil(len(s)/2)):]
    if int(left[::-1]) > int(right):
        return int(left + left[::-1])
    else:
        left = left[:len(left)-1] + str(int(left[len(left)-1]) + 1)
        return int(left + left[::-1])


'''
O(sqrt(n)) time complexity
O(1) space complexity
Checks if a number is prime, fun fact 1 is not prime
'''
import math
def isPrime(n):
    if n == 1 or n == 2:
        return False
    else:
        for i in xrange(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    print minesweeper(5,5,10)
    print count_trailing_zeros_in_fact(25)
    print next_palindome(19)
    print isPrime(73)
