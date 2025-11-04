"""
TC: O(N) {We traverse the input number string once. Each digit is pushed and popped 
           from the stack at most once, resulting in linear time complexity relative to the length of the number.}
SC: O(N) {We use a stack to store digits, which in the worst case may contain all digits of the input number.  
           Therefore, auxiliary space usage is linear.}

Approach:
We are tasked with removing `k` digits from a number string to produce the smallest possible number.

The algorithm uses a monotonic stack to maintain digits in increasing order:
1. Iterate through each digit in the input:
    - While the stack is non-empty, the remaining `k` is positive, and the top of the stack 
      is greater than the current digit, pop from the stack and decrement `k`.
    - Append the current digit to the stack.
2. If `k` digits remain to be removed after the iteration, remove them from the end of the stack.
3. Skip any leading zeros in the resulting stack.
4. Convert the remaining digits back to a string. If the result is empty, return "0".

This greedy approach ensures that at each step, the largest possible digits are removed early, 
leading to the lexicographically smallest number.

This problem ran successfully on Leetcode.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            n = int(n)

            while stack and k>0 and  stack[-1] > n:
                stack.pop()
                k -= 1
            
            stack.append(n)

        if k > 0:
            stack = stack[:-k]
        
        res = ""
        i = 0
        while i < len(stack) and stack[i] == 0:
            i += 1
        
        if not stack[i:]:
            return "0"

        stack = [str(n) for n in stack[i:]]

        return ''.join(stack)
            