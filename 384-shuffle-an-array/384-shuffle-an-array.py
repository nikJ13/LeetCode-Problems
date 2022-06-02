class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.orig = list(nums)

    def reset(self) -> List[int]:
        return self.orig

    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            index = random.randrange(i,len(self.arr))
            self.arr[i], self.arr[index] = self.arr[index], self.arr[i]
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()