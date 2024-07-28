class Solution:
    def __init__(self):
        pass

    def scoreOfString(self, s: str) -> int:
        score = 0 #set up score = 0
        x = list(s) 
        beg = 0
        end = 1 #use beg and end as indexes 
        while end < len(x): #until the second index doesn't go out of range
            score+=abs(ord(x[beg])-ord(x[end])) #do the absolute value of the substraction between the ascii value of the first and the second and add it to the score
            beg+=1
            end+=1 #add the index
        return score
