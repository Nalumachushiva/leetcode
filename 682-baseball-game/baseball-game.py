class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        r=[]
        for op in operations:
            if op=="C":
                r.pop()
            elif op=="D":
                r.append(2*r[-1])
            elif op=="+":
                r.append(r[-1]+r[-2])
            else:
                r.append(int(op))
        return sum(r)