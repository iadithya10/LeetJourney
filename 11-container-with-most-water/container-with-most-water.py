class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Width between the two lines
            width = right - left
            
            # Height of the container (limited by the shorter line)
            current_height = min(height[left], height[right])
            
            # Area formed between the two lines
            area = width * current_height
            
            # Update the maximum area seen so far
            max_water = max(max_water, area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
