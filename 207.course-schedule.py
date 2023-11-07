#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]) -> bool:
        # Create a graph representation with adjacency lists.
        graph = [[] for _ in range(numCourses)]
        
        # Create an array to keep track of the in-degrees of each node.
        in_degree = [0] * numCourses
        
        # Build the graph and in-degrees.
        for pair in prerequisites:
            course, prerequisite = pair
            graph[prerequisite].append(course)
            in_degree[course] += 1
        
        # Initialize a queue for topological sort.
        queue = []
        
        # Add nodes with in-degrees of 0 to the queue.
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Perform topological sort.
        while queue:
            course = queue.pop(0)
            numCourses -= 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        
        return numCourses == 0

        
# @lc code=end

