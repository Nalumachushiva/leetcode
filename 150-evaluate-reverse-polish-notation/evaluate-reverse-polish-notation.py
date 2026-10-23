class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        r=[]
        for i in tokens:
            if i=="+":
                a=r.pop()
                b=r.pop()
                r.append(b+a)
            elif i=="-":
                a=r.pop()
                b=r.pop()
                r.append(b-a)
            elif i=="*":
                a=r.pop()
                b=r.pop()
                r.append(b*a)
            elif i=="/":
                a=r.pop()
                b=r.pop()
                r.append(int(float(b)/(a)))
            else:
                r.append(int(i))
        return r[0]
                