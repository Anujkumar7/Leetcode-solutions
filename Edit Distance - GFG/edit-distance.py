class Solution:
	def editDistance(self, word1, word2):
		# Code here
		m = len(word1)
        n = len(word2)
        t = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            t[i][0] = i
        for j in range(n + 1):
            t[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    t[i][j] = t[i - 1][j - 1]
                else:
                    t[i][j] = 1 + min(t[i - 1][j], t[i][j - 1], t[i - 1][j - 1])
        return t[-1][-1]
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends