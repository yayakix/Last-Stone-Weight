class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        
        while len(stones) > 1:
            stoneY = stones[len(stones) - 1]
            stoneX = stones[len(stones) - 2]
            if stoneX == stoneY:
                stones.pop()
                stones.pop()
            elif stoneX < stoneY:
                stones.pop()
                stones.pop()
                stones.append(stoneY - stoneX)
                stones.sort()
        if len(stones):
            return stones[0]
        else:
            return 0
