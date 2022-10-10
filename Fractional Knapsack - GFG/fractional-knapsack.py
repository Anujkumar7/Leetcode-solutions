#User function Template for python3

class Solution:
        def fractionalknapsack(self, W,Items,n):
        
        # sorting Item on basis of ratio
            Items.sort(key=lambda x: (x.value/x.weight), reverse=True)
 
    # Uncomment to see new order of Items with their
    # ratio
    # for item in arr:
    #     print(item.value, item.weight, item.value/item.weight)
 
    # Result(value in Knapsack)
            finalvalue = 0.0
 
    # Looping through all Items
            for item in Items:
 
        # If adding Item won't overflow, add it completely
                if item.weight <= W:
                    W -= item.weight
                    finalvalue += item.value
 
        # If we can't add current Item, add fractional part
        # of it
                else:
                    finalvalue += item.value * W / item.weight
                    break
    # Returning final value
            return finalvalue
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends