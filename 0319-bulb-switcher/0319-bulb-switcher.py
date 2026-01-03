class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 1 1 1 1 1 1 1 1 1 1
        # 1 0 1 0 1 0 1 0 1 0
        # 1 0 0 0 1 1 1 0 0 0
        # we could calculate the final state of every bulb based on its position
        # second bulb is toggled in rounds => 1,2 only
        # third bulb is toggled in rounds => 1,3 only
        # fourth bulb is toggled in rounds => 1,2 and 4
        # fifth bulb in => 1,5
        # sixth bulb in => 1,2,3,6
        # seventh bulb in => 1,7
        # eight bulb in => 1,2,4,8
        # nineth bulb in => 1,3,9
        # tenth bulb in => 1,2,5,10
        # every nth bulb is toggled in all its factors rounds (excluding one)
        # we just need to get the number of factors of every bulb number
        # the odd number of factors are the ones that will be on towards the end
        # only perfect squares have their bulbs on because they have odd number of factors
        # 1; 1
        # 2; 1
        # 3; 1
        # 4; 2
        # 5; 2
        # 6; 2
        # 7; 2
        # 8; 2
        # 9; 3
        # the number of perfect squares increases in odd numbers
        # n=9; count the number of odd numbers that add upto 9; 3,5,  [3]
        # n= 11
        if n==0:
            return 0
        curr_num = 3
        sum_odds = curr_num
        count = 1
        while sum_odds<n:
            curr_num += 2
            sum_odds += curr_num
            count += 1
        return count

