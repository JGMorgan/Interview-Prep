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


'''
O(n^2) time complexity
O(n) space complexity
Given an array of boxes find the height of the heighest stack
of boxes you can make. You can only stack a box on top of another
box if the base of the box below is smaller than the box on top
boxes is an array of tuples (h,w,d)
'''
def max_height(boxes):
    W = 1
    H = 0
    D = 2
    rotated_boxes = []
    for box in boxes:
        rotated_boxes.append(box)
        rotated_boxes.append((box[W], box[H], box[D]))
        rotated_boxes.append((box[D], box[H], box[W]))

    rotated_boxes.sort(key = lambda box: box[W] * box[D])
    rotated_boxes = rotated_boxes[::-1]

    max_heights = [0 for _ in xrange(len(rotated_boxes) + 1)]

    for i in xrange(1, len(rotated_boxes) + 1):
        max_height_i = 0
        for j in xrange(i):
            if rotated_boxes[j][W] > rotated_boxes[i-1][W] and rotated_boxes[j][D] > rotated_boxes[i-1][D]:
                if max_heights[max_height_i] < max_heights[j+1]:
                    max_height_i = j + 1

        max_heights[i] = max_heights[max_height_i] + rotated_boxes[i-1][H]

    return max_heights[len(max_heights) - 1]



if __name__ == '__main__':
    print max_subarray([2, -1, 2, 3, 4, -5])
    print max_continuous_subarray([2, -1, 2, 3, 4, -5])
    print ways_to_make_change(420)
    print ways_from_topleft_to_bottomleft(6, 5)
    print max_height([(4, 7, 9), (5, 8, 9), (11, 20, 40), (1, 2, 3)])
