# the algorithm uses a hash table, we add the first element of the nums array to the listNum hash table with its index as value,
# then iterate through the rest of elements. If the complement of nums[i] is in listNum return [i, listNum[complement]], if not
# assign i value to listNum[nums[i]]

# Time complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        listNum = {}
        listNum[nums[0]] = 0
        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in listNum:
                return [listNum[complement], i]
            else:
                listNum[nums[i]] = i