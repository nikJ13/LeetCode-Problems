import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Problem: get the count of the max events that can be attended

        Solution: so I can have a min heap, which keeps track of all the events based on the finishing days
        So first arrange the events based on the startdays
        Then declare a heapq
        Then iterate through the events:
            if the heapq is empty, then add that event to it and move on (counter += 1)
            if heapq is not empty,
                pop the first element from the heapq
                pick the last day from heapq[0]
                check if the current start day is lesser than the heapq[0]'s last day
                    if it is smaller or equal to, then add 1 the counter
                    if it is not, then dont do anything
                    add the current event to the queue
        [[1,2],[2,3],[3,4],[1,2]]
        [[1,2],[1,2],[2,3],[3,4]]

        [[1,4],[2,3],[3,4]] => 3
        que = [3,4,4]
        counter = 3

        [[1,1],[1,2],[2,2]] => 2
        [1,2,2]
        que = [1]
        counter = 1

        check the latest end date in the queue, see if a particular day has been occupied or not
        so maybe we could have a list with positions where the day has been visited,
        mark that 1 otherwise 0
        so now suppose the start date is x and end date is y at the beginning, then we want to visit only for 1 day, so the latest available date is y-x+1 if y-x is not zero else if y-x is zero then the date after end date y is the latest available date
        so again, i need to check if the start date is above or equal to the latest available date, if yes, then mark that start date as visited
        if the start date is less than the latest available date, check if the end date is more than the latest available date. If yes, then calculate the new latest available date as end date - latest available date + 1
        else
            leave
        1 2 3
          2 3 4 5

        [[1,5],[1,5],[1,5],[2,3],[2,3]]
        latest_avail = 4
        counter = 3
        """
        events = sorted(events)
        total_events = len(events)
        queue_end_date = []
        day = 0
        i = 0
        counter = 0

        while queue_end_date or i<total_events:
            # if the queue is empty, then the current day is the start date of the first entry of events arr
            if not queue_end_date:
                day = events[i][0]
            
            # then we calculate what all events are there that have the same start date or less than the current start date; add their end dates to the heap
            while i<total_events and events[i][0] <= day:
                heapq.heappush(queue_end_date, events[i][1])
                i += 1
            
            # need to remove all those end dates in the queue that are smaller than the current day
            while queue_end_date and queue_end_date[0]<day:
                heapq.heappop(queue_end_date)
            
            # attend the event that ends the soonest
            if queue_end_date:
                heapq.heappop(queue_end_date)
                counter += 1
            
            day += 1
        return counter

            