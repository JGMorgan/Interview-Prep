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
    print max_subarray([2,-1,2,3,4,-5])
    print max_continuous_subarray([2,-1,2,3,4,-5])
    print ways_to_make_change(420)
    print ways_from_topleft_to_bottomleft(6, 5)
