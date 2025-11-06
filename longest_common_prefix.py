class Solution:
    def longestCommonPrefix(self, strings):
        prefix = strings[0]

        while True:
            if all(word.startswith(prefix) for word in strings):
                return prefix 

            elif len(prefix) == 0:
                return prefix 
            
            else:
                prefix = prefix[:-1]
 