import lib601.search as search
import lib601.sm as sm

search.verbose = True

######################################################################
###
###  Map1 in notes
###
######################################################################

map1 = {'S' : ['A', 'B'],
        'A' : ['S', 'C', 'D'],
        'B' : ['S', 'D', 'E'],
        'C' : ['A', 'F'],
        'D' : ['A', 'B', 'F', 'H'],
        'E' : ['B', 'H'], 
        'F' : ['C', 'D', 'G'],
        'H' : ['D', 'E', 'G'],
        'G' : ['F', 'H']}

search.verbose = True

# 1. Assume the start state is A and the goal state is G.  Enter the path found
# by breadth-first search without dynamic programming.  Enter a sequence of state
# names: A C F G

# 2.	How many states were visited during the search?
# 12

# 3. How many nodes were expanded during the search?
# 6

# 4. Assume the start state is A and the goal state is G.  Enter a path found by
# breadth-first search with dynamic programming.  Enter a sequence of state names.
# A C F G

# 5. How many states were visited during the search?
# 8
# 
# 6. How many nodes were expanded during the search?
# 6

# 7.  Enter the name of a state that was visited more than once by by breadth-first
# without DP.
# F, B

# 8. the path found by breadth-first search with and without DP should generally
# be the same path.
# True

# 9. Enter the maximum number of states that can be visited by ANY breadth-first
# search with DP in map1 (start of the path is not counted as visited).
# 6!

# 10. Assume the start state is G and the goal state is C.  Enter the path found by
# depth-first search without dynamic programming.  Enter a sequence of state names:
# GHEBDFC

# 11. How many states were visited during this search?
# 10
# 
# 12. How many nodes were expanded during this search?
# 6

# 13. Assume the start state is G and the goal state is C.  Enter the path found
# by depth-first search with dynamic programming:
# GHEBSAC

# 14. How many states were visited during this search?
# 8
# 
# 15. How many nodes were expanded during the search?
# 6

# 16. Enter the name of a state that was visited more than once by depth-first 
# without DP.
# D

# 17. Enter the maximum number of states that can be visited by ANY depth-first
# search with DP in map1.
# 12

# 18. The path found by depth-first search with and without DP should generally
# be the same path.
# False

def map1successors(s,a):
	if len(map1[s]) > a: 
		return map1[s][a]
	else:
		return s


print search.search('G',lambda x: x == 'C',range(4),lambda s, a:map1successors(s,a),depthFirst=True,DP=True)