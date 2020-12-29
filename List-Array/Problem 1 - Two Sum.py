# This program is to find the indexes of the numbers which sum upto the target number.
# Here we are creating a dictonary and saving the difference of the target and the number on current index
# as the key and the current index as value.
# Wherever the key will match the number on the current index, the result will be the value of the key
# and current index of the list, hence the same is returned.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if bool(dic) and nums[i] in dic:
                return [dic.get(nums[i]),i]
            else:
                dic.update({(target-nums[i]):i})