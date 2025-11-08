'''
Creates a stack of the open characters and once it encounters a closed character checks if the one on top of the stack 
is the corresponding open. If it is, then pops the one on top of the stack and checks for the other ones. If not 
it stops and returns False.
'''
class Solution:

    def __init__(self):
        self.answer = False
        self.opens = []

    def isValid(self, string):
        self.string = string
        self.list_of_chars = list(self.string)

        if len(self.list_of_chars) % 2 == 1:
            return self.answer
        
        elif len(self.list_of_chars) % 2 == 0:
            for i in range(len(self.list_of_chars)):
                if self.list_of_chars[i] == '(' or self.list_of_chars[i] == '[' or self.list_of_chars[i] == '{':
                    self.opens.append(self.list_of_chars[i])
                
                # It is necessary to have len( self.opens) > 0 since if the list is empty Python cannot check the condition self.opens[-1] == '('
                elif self.list_of_chars[i] == ')' and len(self.opens) > 0 and self.opens[-1] == '(':
                    self.answer = True 
                    self.opens.pop()
                
                elif self.list_of_chars[i] == ']' and len(self.opens) > 0 and self.opens[-1] == '[':
                    self.answer = True 
                    self.opens.pop()

                elif self.list_of_chars[i] == '}' and len(self.opens) > 0 and self.opens[-1] == '{':
                    self.opens.pop()
                    self.answer = True 
                    
                else: 
                    self.answer = False
                    break
        # This condition is necessary, becaus it might happen that you have parentheses that close, but more opens than 
        # the ones that close, making self.opens non-empty. Example "[[[]"           
        if len(self.opens) > 0:
                self.answer = False
        
        return self.answer
 