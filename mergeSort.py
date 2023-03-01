class Sorting:
  def mergeSort(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
            
        mid = len(nums) // 2 
        left = self.mergeSort(nums[0:mid])
        right = self.mergeSort(nums[mid:])

        ans = []

        p1 = 0
        p2 = 0
        
        while p1<len(left) and p2<len(right):
            if left[p1] < right[p2]:
                ans.append(left[p1])
                p1 += 1
            else:
                ans.append(right[p2])
                p2 += 1
        while p1 < len(left):
            ans.append(left[p1])
            p1 += 1
        while p2 < len(right):
            ans.append(right[p2])
            p2 += 1
        
        return ans
