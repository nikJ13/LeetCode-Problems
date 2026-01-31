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
        left,right = [], []
        max_height_left = height[0]
        max_height_right = height[-1]
        ans = 0
        for i in range(len(height)):
            # checking for left
            if max_height_left<=height[i]:
                max_height_left = height[i]
                left.append(0)
            elif max_height_left>height[i]:
                left.append(max_height_left - height[i])

            # checking for right
            idx = len(height) - i - 1
            if height[idx]>=max_height_right:
                max_height_right = height[idx]
                right = [0] + right
            elif height[idx]<max_height_right:
                right = [max_height_right - height[idx]] + right
            
        for i in range(len(height)):
            ans += min(left[i],right[i])
        
        return ans

