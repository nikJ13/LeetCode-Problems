class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_freq = defaultdict(int)
        left_idx_pref_sum = defaultdict(int)
        left_ans = []
        temp = 0
        for i, val in enumerate(nums):
            temp = left_freq[val]*i - left_idx_pref_sum[val]
            left_ans.append(temp)
            left_freq[val]+=1
            left_idx_pref_sum[val] += i
        
        right_freq = defaultdict(int)
        right_idx_pref_sum = defaultdict(int)
        temp = 0
        for j in range(len(nums)-1,-1,-1):
            temp = right_idx_pref_sum[nums[j]] - right_freq[nums[j]]*j
            left_ans[j] += temp
            right_freq[nums[j]] += 1
            right_idx_pref_sum[nums[j]] += j
        return left_ans
