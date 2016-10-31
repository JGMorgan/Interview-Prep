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
	total = sum(x)
	for i in xrange(len(x)):
		if total == 0:
			return i-1
		total -= x[i]

	#if no point found we return -1
	return -1

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
                    print c
                    print temp.table[c].val
                    temp = temp.table[c]
                else:
                    temp.table[c] = Trie()
                    temp.table[c].val = 1
                    print c
                    print temp.table[c].val
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
