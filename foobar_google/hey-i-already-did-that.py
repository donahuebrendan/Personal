'''
Hey, I Already Did That!
========================

Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep her minions on their toes. But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion. 

You have worked out that the algorithm has the following process: 

1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases -- 
Input:
Solution.solution('210022', 3)
Output:
    3

Input:
Solution.solution('1211', 10)
Output:
    1

-- Python cases -- 
Input:
solution.solution('1211', 10)
Output:
    1

Input:
solution.solution('210022', 3)
Output:
    3

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

'''

minion_ids = []

input_n = 1211
input_b = 10

def sort(nin):
    output = list(str(nin))
    a_sort = sorted(output)
    d_sort = a_sort[::-1]
    
    a_sort = str(''.join(str(i) for i in a_sort))
    d_sort = str(''.join(str(i) for i in d_sort))
    return a_sort, d_sort

def ternary (n, y, k):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, y)
        nums.append(str(r))
    output =  ''.join(reversed(nums))

    while len(str(output)) < k:
        output = "0" + str(output)
    return output

def smart_subtract(x, y, k):
    output = x - y

    while len(str(output)) < k:
        output = "0" + str(output)

    return int(output)

def functiony(minion, b, k):
    while 1:
        yin, xin = sort(minion)
        x = int(xin, b)
        y = int(yin, b)

        out = smart_subtract(x, y, k)

        temp = ternary(out, b, k)

        if minion_ids.count(temp) > 1:
           break
        
        else:
    
            minion_ids.append(temp)

            minion = temp

    return temp

def pattern(seq, loop_start):
    start = 0
    n = 0
    for i in seq:
        if i == loop_start and start == 1:
            break
        if i == loop_start and start == 0:
            start = 1
            n +=1
        if i != loop_start and start == 1:
            n += 1
    return n        

def solution(n, b):
    loop_start = functiony(n, b, len(str(n)))
    loop = pattern(minion_ids, loop_start)
    return loop

n = 210022 # input n
b = 3 # input b

# main function for google
final_out = solution(n, b)
print final_out
