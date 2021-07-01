from edge import Edge
from graph import Graph
from kruskal import Kruskal
from random import randint, choice
from string import ascii_letters
import random
import string

g = Graph()
#----------Graph 1--------------
e1 = Edge(0, 1, 4)	
e2 = Edge(0, 2, 3)	
e3 = Edge(0, 6, 6)	
e4 = Edge(1, 3, 3)	
e5 = Edge(1, 7, 5)	
e6 = Edge(2, 3, 4)	
e7 = Edge(2, 4, 5)	
e8 = Edge(3, 5, 6)	
e9 = Edge(4, 5, 3)
e10 = Edge(4, 6, 6)	
e11 = Edge(5, 7, 2)
e12 = Edge(6, 7, 7)
					
g.insert(e1)			
g.insert(e2)			
g.insert(e3)			
g.insert(e4)			
g.insert(e5)			
g.insert(e6)
g.insert(e7)			
g.insert(e8)			
g.insert(e9)			
g.insert(e10)			
g.insert(e11)
g.insert(e12)
#------------------------

#----------Graph 2--------------
# e1 = Edge(0, 1, 4)
# e2 = Edge(0, 5, 2)
# e3 = Edge(0, 4, 1)
# e4 = Edge(1, 4, 2)
# e5 = Edge(1, 2, 2)
# e6 = Edge(2, 3, 8) 
# e7 = Edge(3, 4, 3)
# e8 = Edge(3, 5, 6)
# e9 = Edge(4, 5, 7)
				
				
# g.insert(e1)	
# g.insert(e2)	
# g.insert(e3)	
# g.insert(e4)	
# g.insert(e5)	
# g.insert(e6)	
# g.insert(e7)	
# g.insert(e8)	
# g.insert(e9)	
				
#-------Program-----------------

k = Kruskal(g)

k.algorithm()