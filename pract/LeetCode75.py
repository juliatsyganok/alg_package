class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = [0, 0, 0]
        for i in nums:
            count[i] += 1
        
        ind = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[ind] = color
                ind += 1
        