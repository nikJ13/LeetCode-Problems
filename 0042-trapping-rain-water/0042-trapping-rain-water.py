class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Problem: Find all the water that is accumulated in between the valleys of the bars
        Solution: 

        [0,1,0,2,1,0,1,3,2,1,2,1]
        
        left =    [0,0,1,0,1,2,1,0,1,2,1,2]

        right =   [3,2,3,1,2,3,2,0,0,1,0,0]

        min_arr = [0,0,1,0,1,2,1,0,0,1,0,0]

        max_height_left = 0,1,2,3,
        water_stored_left = 11

        max_height_right = 1,2,3
        water_stored_right = 

        Condition to handle the edge case:
        max_height = height[0]
        if max_height<=height[i]:
            max_height = height[i]
        if max_height>height[i]:
            then you must measure the water stored above the height[i] block
            water_stored += max_height - height[i]
        """
        left, right = 0, len(height)-1
        max_left, max_right = height[0], height[-1]
        ans = 0
        while left<right:
            if height[left]<height[right]:
                if max_left<=height[left]:
                    max_left = height[left]
                else:
                    ans += max_left - height[left]
                left += 1
            else:
                if height[right]>=max_right:
                    max_right = height[right]
                else:
                    ans += max_right - height[right]
                right -= 1
        return ans

