class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=0
        stack=[]
        for i in s:
            if i=="(":
                if c>0:
                    stack.append(i)
                c+=1
            elif i==")":
                c-=1
                if c>0:
                    stack.append(i)
        return "".join(stack)          