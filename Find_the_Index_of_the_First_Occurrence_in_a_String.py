class Solution:
    def strStr(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle 

        if self.needle in self.haystack:
            return self.haystack.find(self.needle) 
        
        else:
            return -1 
        
 
        