"""
TC: O(N) {We traverse the list of tokens once, performing constant-time operations 
           (push/pop and arithmetic) for each token. Hence, the overall time complexity is linear in the number of tokens.}
SC: O(N) {We use a stack to store operands, which in the worst case may contain all numbers from the input.  
           Therefore, auxiliary space usage is linear in the number of tokens.}

Approach:
We are tasked with evaluating an expression given in Reverse Polish Notation (RPN), 
where each token is either an integer or an operator (+, -, *, /).

The algorithm uses a stack to maintain operands:
1. Iterate through each token in the input list:
    - If the token is a number, push it onto the stack.
    - If the token is an operator:
        - Pop the two most recent numbers from the stack.
        - Apply the operator (taking care of order for subtraction and division).
        - For division, truncate toward zero (matching integer division behavior).
        - Push the result back onto the stack.
2. After processing all tokens, the stack contains a single element, 
   which is the final result of the RPN expression.

This stack-based approach ensures correct evaluation order and handles operators efficiently.

This problem ran successfully on Leetcode.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ['+', '-', '*','/']
        stack = []

        for i in range(len(tokens)):
            curr = tokens[i]
            if curr not in opr:
                stack.append(int(curr))
            else:
                one, two = stack.pop(), stack.pop()
                if curr == "+":
                    ans = one + two
                elif curr  == "*":
                    ans = one * two
                elif curr == "-":
                    ans = two - one
                else:
                    ans = two / one
                    if ans < 0.0:
                        ans = int(ceil(ans))
                    else:
                        ans = int(floor(ans))

                stack.append(ans)

        return stack[0]

