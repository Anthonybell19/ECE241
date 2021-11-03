"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2021
question3.py - DP planks with turtle
"""


class Solution:
    def solve(self):
        ''' TREE TRAVERSAL
            - Select a traversal scheme answer each of the questions below.
             options: (DFS, BFS, BOTH)

             - Select BOTH if the order of traversal makes no difference.
        '''
        ans = None

        ''' EXAMPLE
        Find the minimum element in a binary search tree '''
        ans = "DFS"
        print(ans)

        ''' 1
        Given a node n, find its nearest neighbour'''
        ans = 'BFS'
        print(ans)

        ''' 2
        Find the shortest path between 2 vertices(nodes) in a graph.'''
        ans = 'BOTH'
        print(ans)

        ''' 3
        Find the shortest cycle in a directed graph'''
        ans = 'DFS'
        print(ans)

        ''' 4
        Find the longest cycle in a directed graph'''
        ans = 'DFS'
        print(ans)

        ''' 5
        Which tree traversal scheme uses more memory'''
        ans = 'BFS'
        print(ans)

        ''' 6
        Which traversal scheme can be implemented using a queue'''
        ans = 'BFS'
        print(ans)

        ''' 7
        Finding the destination of a packet routed through a network'''
        ans = 'BOTH'
        print(ans)


if __name__ == "__main__":
    sol = Solution()
    sol.solve()