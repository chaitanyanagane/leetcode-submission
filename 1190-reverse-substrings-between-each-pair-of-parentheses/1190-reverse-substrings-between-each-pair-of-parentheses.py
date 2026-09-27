class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        
        # Precompute matching bracket indices
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i
        
        result = []
        i, d = 0, 1  # d = direction: 1 = forward, -1 = backward
        
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]   # jump to matching bracket
                d = -d        # flip direction
            else:
                result.append(s[i])
            i += d
        
        return ''.join(result)