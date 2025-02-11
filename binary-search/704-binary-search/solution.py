class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            current_index = l + ((r - l) // 2)

            if nums[current_index] > target:
                r = current_index - 1
            elif nums[current_index] < target:
                l = current_index + 1
            else:
                return current_index

        return -1
