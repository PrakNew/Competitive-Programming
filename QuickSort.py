class Solution:
    def quickSort(self, nums, low, high):

        # Low >= High then no elemnts to process in between
        if low >= high or low < 0:
            return

        pivot  = self.partition(nums, low, high)
        self.quickSort(nums, low, pivot - 1)
        self.quickSort(nums, pivot + 1, high)


    def partition(self, nums, low, high):

        mid = (low + high) // 2
        # For a sorted list this will move the pivot to the middle of the list.
        # Eg: 1, 2, 3, (4), 5, 6, 7, 8, 9, (10)
        # Becomes: 1, 2, 3, (10), 5, 6, 7, 8, 9, (4)
        # Now if pivot is last number then the final swap will return index 3 instead of index 9
        # Since in sorted case it will move a smaller number to end of list, swaps will stop after mid
        nums[high], nums[mid] = nums[mid], nums[high]
        swap_idx = low # Place where a number smaller than pivot should be placed

        for start in range(low, high):
            if nums[start] <= nums[high]:
                nums[start], nums[swap_idx] = nums[swap_idx], nums[start]
                swap_idx += 1
        
        nums[high], nums[swap_idx] = nums[swap_idx], nums[high]
        return swap_idx

def partition(a,p,r):
	key=a[r]
	i=p-1
	for j in range(p,r):
		if a[j]<=key:
			i+=1
			a[i],a[j]=a[j],a[i]
	a[i+1],a[r]=a[r],a[i+1]
	return i+1
def quicksort(a,p,r):
	if p<r:
		q=partition(a,p,r)
		quicksort(a,p,q-1)
		quicksort(a,q+1,r)
p=[4,3,2,1,8,3,4]
quicksort(p,0,len(p)-1)
print(p)
