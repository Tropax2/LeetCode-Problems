class Solution:
    def removeElement(self, nums, val):
        self.nums = nums
        self.val = val
        self.k = 0
        for i in range(len(self.nums)):
            if self.nums[i] != self.val:
                self.nums[self.k] = self.nums[i]
                self.k += 1

        return self.k, self.nums[:self.k]
 
