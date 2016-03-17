def remove(s):
	if not s:
		return ''
	for c in sorted(set(s)):
		suffix=s[s.index(c):]
		if set(suffix)==set(s):
			return c + remove(suffix.replace(c,''))

def remove2(s):
	res=''
	while s:
		idx=min(map(s.rindex,set(s)))
		c=min(s[:idx+1])
		s=s[s.index(c):].replace(c,'')
		res+=c
	return res

def remove3(s):
	result = ''
	for i, c in enumerate(s):
	    if c not in result:
	        while c < result[-1:] and i < s.rindex(result[-1]):
	            result = result[:-1]
	        result += c
	return result


def isValidSerialization(preorder):
    need = 1
    for val in preorder.split(','):
    	print val
        if not need:
            return False
        need -= ' #'.find(val)
        print need
    return not need

isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
