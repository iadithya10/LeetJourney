class Solution(object):
    def twoSum(self, num, target):
        left=0
        right=len(num)-1
        while left<right:
            s=num[left]+num[right]
            if s==target:
                return [left+1,right+1]
            elif s<target:
                left+=1
            else:
                 right-=1
       
        