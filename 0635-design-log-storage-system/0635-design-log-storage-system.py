class LogSystem:

    def __init__(self):
        self.dict_logs = {}
        self.components = {"Year":4,"Month":7,"Day":10,"Hour":13,"Minute":16,"Second":19}

    def put(self, id: int, timestamp: str) -> None:
        self.dict_logs[id] = timestamp
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start_compare = start[:self.components[granularity]]
        end_compare = end[:self.components[granularity]]
        ans = []
        for logs in self.dict_logs:
            curr_compare = self.dict_logs[logs][:self.components[granularity]]
            if start_compare<=curr_compare<=end_compare:
                ans.append(logs)
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)