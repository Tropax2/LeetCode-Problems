class Solution:

    def isPalindrome(self, palindrome):
        self.palindrome = str(palindrome)
        self.palindrome_reversed = self.palindrome[::-1]
        if self.palindrome == self.palindrome_reversed:
            return True 
        else:
            return False 


