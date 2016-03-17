class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        #l=list(s)
        stack=[]
        sign=1
        tmp=0
        for c in s:
        	if c.isdigit():
        		tmp=10*tmp+int(c)
        	elif c in '+-':
        		res+=sign*tmp
        		tmp=0
        		sign=[-1,1][c=='+']
        	elif c=='(':
        		stack.append(res)
        		stack.append(sign)
        		sign=1
        		res=0
        	elif c==')':
				res+=sign*tmp
				res*=stack.pop()
				res+=stack.pop()
				tmp=0
       	return res

s='( 1-(4+(5- (5 - 6)+ 7)-9) )'
sl=Solution()
print sl.calculate(s)