"""
Problem Statement:
You are given a 2D grid of size n x n, where each cell can either be:
- 1 (a valid cell that can be traversed)
- 0 (an obstacle that cannot be traversed)

You start at the top-left corner of the grid (position (0, 0)) and need to reach the bottom-right corner (position (n-1, n-1)).
You can only move in four directions: right (R), down (D), left (L), and up (U).

Your task is to find all possible paths from the start to the destination, and return these paths as a list of strings,
where each string represents a series of moves made to reach the destination.

Constraints:
- The grid is represented by a list of lists (2D array).
- You should not revisit cells (mark them as visited) to avoid cycles.
- If there are no valid paths, return an empty list.
"""

from typing import List  # Importing List from typing module for type hinting

def findPath(m: List[List[int]]) -> List[str]:
    ans = []  # Initialize a list to store the valid paths
    
    def rec(m, i, j, st):
        # Base case: check if current position is out of bounds or already visited or blocked
        if i >= len(m) or j >= len(m[0]) or i < 0 or j < 0 or m[i][j] == -1 or m[i][j] == 0:
            return  # Return if out of bounds or cell is visited (-1) or blocked (0)
        
        # Check if we have reached the destination
        if i == len(m) - 1 and j == len(m[0]) - 1:
            ans.append(st)  # Append the path string to the results
            return  # Return after adding the valid path

        # NOTE: you can use m[i][j] = 0 itself for marking the visited cell, but here I have used m[i][j] = -1 separately for better understanding.
        m[i][j] = -1  # Mark the current cell as visited by setting it to -1
        
        # Explore the four possible directions:
        rec(m, i, j + 1, st + 'R')  # Move Right and add 'R' to the path
        rec(m, i + 1, j, st + 'D')  # Move Down and add 'D' to the path
        rec(m, i, j - 1, st + 'L')  # Move Left and add 'L' to the path
        rec(m, i - 1, j, st + 'U')  # Move Up and add 'U' to the path
        
        m[i][j] = 1  # Reset the current cell back to unvisited (1) for future explorations
    
    rec(m, 0, 0, "")  # Start the recursion from the top-left corner (0, 0) with an empty path
    return ans  # Return all found paths

if __name__ == "__main__":
    m = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    
    paths = findPath(m)
    
    print("All Paths:")
    for path in paths:
        print(path)
