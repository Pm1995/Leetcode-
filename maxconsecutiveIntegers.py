#Input: [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s.
    #The maximum number of consecutive 1s is 3.
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        num=0
        ans=0
        for i in nums:
            if i!=0:
                num=num+1
            else:
                if ans>num:
                    num =0 
                    continue
                else:
                    ans=num
                    num=0
        if ans>num:
	        return(ans)
        else:
	        return(num)
        	


