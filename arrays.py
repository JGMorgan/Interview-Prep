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


if __name__ == '__main__':
    print mid_point([1,2,3,4,5])
    print mid_point([2,-1,2,3,4,-4])
    print swap_no_temp_variable([1,2,3],0,2)
