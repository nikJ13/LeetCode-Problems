class TimeMap:

    def __init__(self):
        self.store = {}

        """
        so I was thinking of this:
        "key":{"ts1":val1, "ts2":val2, "ts3":val3}
        keep a prev ts tracker for each key
        we can use binary search to search for the desired timestamp

        [[],["foo","bar",5],["foo","bar2",10],["foo","bar3",14],["foo",4],["foo",6],["foo",11]]

        {"foo":[(5,"bar"),(10,"bar2"),(14,"bar3")]}
        target_val = 6
        start = 0
        end = 2
        mid = 1

        """


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def binary_search(self,target_val,ref_list):
        #print(ref_dict)
        ans = ""
        start, end = 0, len(ref_list)-1
        while start<=end:
            #print(start,end)
            mid = (start+end)//2
            ts, val = ref_list[mid]
            if ts<=target_val:
                ans = val
                start = mid + 1
            else:
                end = mid - 1
        return ans

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        target_list = self.store[key]
        curr_ts = timestamp
        res = self.binary_search(curr_ts,target_list)
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)