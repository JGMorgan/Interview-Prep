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
Check if an integer is a power of 2
'''
def isPowerOfTwo(n):
    return n & (n-1) == 0


if __name__ == '__main__':
    print count_1_bits(10)
    print how_many_flips(10,5)
    print isPowerOfTwo(128)
