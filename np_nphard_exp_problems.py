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


if __name__ == '__main__':
    print powerset([1,2,3])
    print perms_of_string('abc')
