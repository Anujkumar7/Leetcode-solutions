class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        color_to_change = image[sr][sc]
        
        def dfs(r, c):
            nonlocal rows, cols, newcolor, image
            
            if r< 0 or c< 0 or r>rows-1 or c>cols-1 or image[r][c]== newcolor or                image[r][c]!= color_to_change:
                return
            
            image[r][c] = newcolor
            
            #radiate in four direction
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            
        dfs(sr, sc)
        return image
                