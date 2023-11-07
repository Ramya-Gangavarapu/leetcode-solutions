#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]) -> List[int]:
        # Create a graph representation with adjacency lists.
        graph = [[] for _ in range(numCourses)]
        
        # Create an array to keep track of the in-degrees of each course.
        in_degree = [0] * numCourses
        
        # Build the graph and in-degrees.
        for pair in prerequisites:
            course, prerequisite = pair
            graph[prerequisite].append(course)
            in_degree[course] += 1
        
        # Initialize a queue for topological sort.
        queue = []
        
        # Add courses with in-degrees of 0 to the queue.
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Initialize a list to store the topological order.
        topological_order = []
        
        # Perform topological sort.
        while queue:
            course = queue.pop(0)
            topological_order.append(course)
            numCourses -= 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If there are no cycles (all courses were taken), return the topological order.
        return topological_order if numCourses == 0 else []

        
# @lc code=end

