class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append((timestamp, 0))

    def getHits(self, timestamp: int) -> int:
        starting_ts = timestamp - 300 + 1
        if starting_ts<0:
            return len(self.hits)
        count = 0
        #print(self.hits)
        for ts, _ in self.hits:
            if ts>=starting_ts:
                count += 1
        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)