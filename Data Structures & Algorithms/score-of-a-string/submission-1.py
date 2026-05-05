class Solution:
    def scoreOfString(self, s: str) -> int:

    	t_sum = 0

    	for c in range(len(s) -1):
    		n = c + 1
    		
    		t_sum += abs(ord(s[c]) - ord(s[n]))
    	return t_sum



