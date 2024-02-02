class Solution:
    def find_target (self, nums, target):
        last_index = len(nums) - 1
        
        for index in range(last_index):
            final_target = nums[last_index] + nums[index]
            
            if final_target == target:
                return final_target, [index, last_index]
            
        return final_target, None
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_target = None

        while final_target != target:
            final_target, result = self.find_target(nums, target)
            nums.pop()
            
        return result
            
