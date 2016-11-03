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
O(2^n) time complexity
O(2^n) space complexity
returns the powerset of a set
'''
def powerset(x):
    out = [[]]
    for elem in x:
        for elem2 in out:
            temp = []
            temp += elem2 + [elem]
        out.append(temp)
    return out


'''
O(n!) time complexity
O(n!) space complexity
returns all permutations of
a given string
'''
def perms_of_string(x):
    return perms_of_string_help(x,'',[])

def perms_of_string_help(start,end,li):
    if len(start) == 0:
        li.append(end)
    else:
        for i in xrange(len(start)):
            s2 = start[:i] + start[i+1:]
            end2 = end + start[i]
            perms_of_string_help(s2, end2, li)
    return li


'''
O(n) time complexity
O(1) space complexity
returns the max sum that any subset
of a given set can have
'''
def max_subarray(x):
    biggest = 0
    for elem in x:
        if biggest + elem < elem and biggest < elem:
            biggest = elem
        elif biggest < biggest + elem:
            biggest += elem
    return biggest


'''
O(n) time complexity
O(1) space complexity
returns the max sum of a consecutive
sub list in a list
'''
def max_continuous_subarray(x):
    biggest = 0
    this_subarray = 0
    for elem in x:
        if this_subarray > biggest:
            biggest = this_subarray
        if this_subarray + elem < elem and this_subarray < elem:
            this_subarray = elem
        else:
            this_subarray += elem
    return biggest


'''
O(n) time complexity
O(1) space complexity
Given a list find a point where the sum of
the elements on the left == the sum of the
elements on the right
'''
def mid_point(x):
    total = sum(x)/2
    length = len(x)
    secondLoop = False
    mid_point = -1
    for i in xrange(length):
        if total == 0:
            if secondLoop:
                return mid_point
            else:
                secondLoop = True
                total = sum(x)/2
                mid_point = i-1
        total -= x[i]
    #if no point found we return -1
    return mid_point


'''
O(1) time complexity since it can only run atmost 64 time
O(number of 1 bits) is also a valid time complexity
O(1) space complexity
count the number of 1 bits in an int
'''
def count_1_bits(n):
    total = 0
    while n != 0:
        total += 1
        n = n & n-1
    return total


'''
O(1) time complexity since it can only run atmost 64 time
O(number of 1 bits) is also a valid time complexity
O(1) space complexity
How many bits need to be flipped to make
two integers equal to eachother
'''
def how_many_flips(a,b):
    x = a^b
    return count_1_bits(x)


'''
O(1) time complexity
O(1) space complexity
swap two elements in a list without
using any temporary variables
'''
def swap_no_temp_variable(li, x, y):
    li[x] += li[y]
    li[y] = li[x] - li[y]
    li[x] -= li[y]
    return li


'''
O(n*m) time complexity where m is the length of the longest string
O(m) space complexity since each hashmap can only contain 26 keys
Find shortest unique prefix to represent each word in the list.
This question didn't make much sense to me when
I first read it but basically you are supposed
return the shortest prefix that doesn't exist in any other word
if given ['dog', 'duck'] both begin with 'd' so the shortest prefixes
are ['do', 'du']
'''
class Trie:
    def __init__(self):
        self.table = {}
        self.val = 0

def prefix(A):
    out = []
    trie = Trie()
    for x in A:
        temp = trie
        for c in x:
            if c in temp.table:
                temp.table[c].val += 1
                temp = temp.table[c]
            else:
                temp.table[c] = Trie()
                temp.table[c].val = 1
                temp = temp.table[c]
    for i in xrange(len(A)):
        temp = trie
        out.append('')
        for c in A[i]:
            if temp.table[c].val == 1:
                out[i]+=c
                break
            else:
                temp = temp.table[c]
                out[i]+=c
    return out


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
O(1) time complexity
O(1) space complexity
Check if an integer is a power of 2
'''
def isPowerOfTwo(n):
    return n & (n-1) == 0


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


'''
O(n) time complexity
O(n) space complexity
Given an infinite amount of pennies, dimes,
nickels and quarters how many ways can we make
n cents
'''
def ways_to_make_change(n):
    coins = [1,5,10,25]
    table = [[0 for _ in xrange(len(coins))] for _ in xrange(n+1)]
    #how many ways can we make 0 cents with our coins
    #there is only 1 way to make any amount with only pennies
    for i in xrange(len(coins)):
        table[0][i] = 1
    for i in xrange(n+1):
        table[i][0] = 1
    for i in xrange(1, n+1):
        for j in xrange(1, len(coins)):
            x = 0
            if i - coins[j] >= 0:
                x = table[i - coins[j]][j]
            y = table[i][j-1]
            table[i][j] = x + y
    return table[n][len(coins)-1]


'''
O(m*n) time complexity
O(m*n) space complexity
Given an m x n matrix, how many ways can you get from
the top left to the bottom left of the matrix assuming
you can move right, down and bottom right
'''
def ways_from_topleft_to_bottomleft(m, n):
    table = [[0 for _ in xrange(m)] for _ in xrange(n)]
    for i in xrange(m):
        table[0][i] = 1
    for i in xrange(n):
        table[i][0] = 1
    for i in xrange(1, n):
        for j in xrange(1, m):
            table[i][j] = table[i-1][j-1] + table[i][j-1] + table[i-1][j]
    return table[n-1][m-1]


if __name__ == '__main__':
    print count_trailing_zeros_in_fact(25)
    print powerset([1,2,3])
    print perms_of_string('abc')
    print max_subarray([2,-1,2,3,4,-5])
    print max_continuous_subarray([2,-1,2,3,4,-5])
    print mid_point([1,2,3,4,5])
    print mid_point([2,-1,2,3,4,-4])
    print count_1_bits(10)
    print how_many_flips(10,5)
    print swap_no_temp_variable([1,2,3],0,2)
    print prefix([ "zebra", "dog", "duck", "dot" ])
    print next_palindome(19)
    print minesweeper(5,5,10)
    print isPowerOfTwo(128)
    print isPrime(73)
    print ways_to_make_change(420)
    print ways_from_topleft_to_bottomleft(6, 5)
