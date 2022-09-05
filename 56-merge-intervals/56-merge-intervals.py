class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        
        # i stands for the interval and i[0]= starting from 0th value
        intervals.sort(key= lambda i : i[0])
        
        #Storing the intervals in output
        output = [intervals[0]]
        
        #Ignoring the first value in the list because we already added up there
        for start,end in intervals[1:]:
            lastend = output[-1][1]
            
        #Checking if the intervals are merging or not     
            if start<= lastend:
                
        # ex: [1,5], [2,4] = [1,5] so we are choosing the max of last value
                output[-1][1] = max(lastend, end)
            else:
                output.append([start,end])
        return output
    
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # predefined constant for start (left endpoint), and end (right endpoint)
        START, END = 0, 1
        
        result = []
        
        # make all intervals sorted on (left endpoint, right endpoint) pair in ascending order
        intervals.sort( key = lambda x: (x[START], x[END] ) ) 
        
        for interval in intervals:
            
            if not result or ( result[-1][END] < interval[START] ):
				# no overlapping
                result.append( interval )
            
            else:
				# has overlapping
				# merge with previous interval
                result[-1][END] = max(result[-1][END], interval[END])
                
        return result