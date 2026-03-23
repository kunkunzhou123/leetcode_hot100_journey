"""
1.初始版本
思路：双指针，快指针遍历数组，慢指针记录非零元素的位置，当快指针遇到非零元素时，将其与慢指针位置的元素交换，并将慢指针向前移动一位。
时间复杂度：O(n)，其中 n 是数组的长度。快指针需要遍历整个数组一次。
空间复杂度：O(1)，只使用了常数级别的额外空间。
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow,fast=0,0
        l=len(nums)
        for fast in range(l):
            if nums[fast]!=0:
                while slow<fast and nums[slow]!=0:
                    slow+=1
                if nums[slow]==0:
                    nums[slow]=nums[fast]
                    nums[fast]=0
                    slow+=1
        return nums

"""
2.优化版本(claude)
思路：同样使用双指针，快指针遍历数组，找到不为0的元素时，将其与慢指针位置的元素交换，并将慢指针向前移动一位。相比于方法一少了一个while循环，不需要判断慢指针位置的元素是否为0，因为快指针遇到非零元素时，慢指针位置必定是0。(同时指向非零元素时，原地交换不会出现快慢差，但会把slow往后推一位，只有当slow确实指向0的时候，此时有了快慢差，fast指向非0，交换才是有效的。)
时间复杂度：O(n)，其中 n 是数组的长度。快指针需要遍历整个数组一次。
空间复杂度：O(1)，只使用了常数级别的额外空间。
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums


                
            