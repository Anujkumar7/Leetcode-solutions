# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res =[]
    #We are using preorder traversal     
    
        def dfs(root):
            if not root:
                
     #Creating a specoial character for defining null           
                res.append("N")
                return
        
        #Appending the values in string format
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
       #Returning res with our delimiter , 
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        
    #We know that our data is already delimitered with str"," we have to remove those delimmeter    
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            
   #Base case (Checking if our val is None by that string "N")         
            if vals[self.i]== "N":
                self.i+=1
                return None
            
    #We know that the values in str we have to Convert them to int
            root =TreeNode(int(vals[self.i]))
            self.i +=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))