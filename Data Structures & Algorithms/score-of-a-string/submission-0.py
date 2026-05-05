class Solution:
    def scoreOfString(self, s: str) -> int:

    	t_sum = 0

    	for c in range(len(s) -1):
    		n = c + 1
    		b = ord(s[c]) if ord(s[c]) > ord(s[n]) else ord(s[n])

    		h = ord(s[c]) if ord(s[c]) < ord(s[n]) else ord(s[n])
    		t_sum += b - h
    	return t_sum

