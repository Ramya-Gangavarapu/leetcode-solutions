#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional, Dict, List

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        
        node_map = {}
        
        
        queue = [node]

        
        cloned_node = Node(node.val)
        node_map[node] = cloned_node

        while queue:
            current_node = queue.pop(0)
            for neighbor in current_node.neighbors:
                if neighbor not in node_map:
                    
                    new_neighbor = Node(neighbor.val)
                    node_map[neighbor] = new_neighbor
                    queue.append(neighbor)

                
                node_map[current_node].neighbors.append(node_map[neighbor])

        return node_map[node]

        
# @lc code=end

