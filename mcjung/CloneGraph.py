# solution Link: https://leetcode.com/submissions/detail/265920003/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.node_ref = {}
        return self._clone_graph(node)
    
    def _clone_graph(self, old_node: 'Node') -> 'Node':
        if old_node in self.node_ref:
            return self.node_ref[old_node]
        
        new_node = Node(old_node.val, [])
        self.node_ref[old_node] = new_node
        for node in old_node.neighbors:
            new_node.neighbors.append(self._clone_graph(node))
        
        return new_node
            
        
        
