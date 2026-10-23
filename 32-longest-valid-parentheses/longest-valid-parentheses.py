class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        stack=[-1]
        for ind,ch in enumerate(s):
            if ch=="(":
                stack.append(ind)
            else:
                stack.pop()
                if not stack:
                    stack.append(ind)
                else:
                    res=max(res,ind-stack[-1])
        return res