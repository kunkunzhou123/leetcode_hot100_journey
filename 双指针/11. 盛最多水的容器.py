""" 
1.初始版本
思路：双指针，左右指针往中间走，更新短边，计算面积，更新最大面积。
时间复杂度：O(n)，其中 n 是数组的长度。左右指针需要遍历整个数组一次。
空间复杂度：O(1)，只使用了几个变量:maxsum, currentsum, left, right。
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxsum=0
        currentsum=0
        left=0
        right=len(height)-1
        while left<right:
            if height[left]<height[right]:
                currentsum=(right-left)*min(height[right],height[left])
                maxsum=max(maxsum,currentsum)
                left+=1
            else:
                currentsum=(right-left)*min(height[right],height[left])
                maxsum=max(maxsum,currentsum)
                right-=1
        return maxsum
    
""" 
2.优化版本(claude)
简化了一下代码，去掉了currentsum变量，直接在计算面积时更新maxsum。
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxsum = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            # 计算当前面积
            maxsum = max(maxsum, (right - left) * min(height[left], height[right]))
            
            # 移动较矮的指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxsum
        