"""
1.初始版本
思路：排序+双指针，先对数组进行排序，然后使用双指针。
注意：j,k跳过重复值的时候不要多跳。
时间复杂度：O(n^2)，其中 n 是数组的长度。排序需要 O(n log n)，双指针需要 O(n)。
总时间 = 排序 + 双重循环
       = O(n log n) + O(n) × O(n)
       = O(n log n) + O(n²)
       = O(n²)  ← 取最大项
空间复杂度：O(n)，排序需要 O(n) 的空间复杂度。  
优化点：if nums[i] > 0:
             break
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                ans=nums[i]+nums[j]+nums[k]
                if ans<0:
                    j+=1
                elif ans>0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
                    while k>j and nums[k]==nums[k+1]:
                        k-=1
        return res
            


            
        