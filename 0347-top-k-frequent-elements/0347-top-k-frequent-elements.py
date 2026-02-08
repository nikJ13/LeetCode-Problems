import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Problem: return the k most frequent elements
        Solution:
        Naive => keep track of the frequencies of the numbers and then use a heapq to store the top k most frequent numbers
        finally get all the numbers in the heapq
        But we want something better than O(nlogn)
        """
        dict_freq = {}
        for i in range(len(nums)):
            if nums[i] not in dict_freq:
                dict_freq[nums[i]] = 0
            dict_freq[nums[i]] += 1
        queue = []
        heapq.heapify(queue)
        # [-1,4]
        for key in dict_freq:
            if len(queue)<k:
                heapq.heappush(queue,(dict_freq[key],key))
            else:
                freq, head = queue[0]
                if freq < dict_freq[key]:
                    heapq.heapreplace(queue,(dict_freq[key],key))
        ans = []
        for f,a in queue:
            ans.append(a)
        return ans