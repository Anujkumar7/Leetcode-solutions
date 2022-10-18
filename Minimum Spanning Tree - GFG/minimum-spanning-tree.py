#User function Template for python3
import sys
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        key = [sys.maxsize]*V
        parent = [-1]* (V)
        visited = [False]*(V)
        
        key[0] = 0
        parent[0]= -1
        
        for i in range(V):
            #Find minimum key value node
            mini = sys.maxsize
            minNode = 0
            for j in range(V):
                if visited[j]== False and key[j]< mini:
                    minNode = j
                    mini = key[j]
            visited[minNode] = True
            
            for node, dis in adj[minNode]:
                if visited[node] == False and dis< key[node]:
                    parent[node] = minNode
                    key[node] = dis
        return sum(key)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends