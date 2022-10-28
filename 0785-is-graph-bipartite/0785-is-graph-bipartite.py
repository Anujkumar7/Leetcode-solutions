class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour = [None]* len(graph)
        for i in range (len(graph)):
            if colour[i] is None:
                colour[i]= 1
                queue = [i]
                while queue:
                    currentnode = queue.pop(0)
                    for node in graph[currentnode]:
                        if colour[node] is None:
                            colour[node] = 1- colour[currentnode]
                            queue.append(node)
                        elif colour[node] == colour[currentnode]:
                            return False
        return True
                            
        