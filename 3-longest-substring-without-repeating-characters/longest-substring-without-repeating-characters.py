class Solution(object):
    def lengthOfLongestSubstring(self,s):
        left=0
        max_len=0
        last_seen={}
        for right ,ch in enumerate(s):
            if ch in last_seen and last_seen[ch]>=left:
                left=last_seen[ch]+1
            last_seen[ch]=right
            max_len=max(max_len,right-left+1)
        return max_len