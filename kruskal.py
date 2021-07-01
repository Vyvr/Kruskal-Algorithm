from edge import Edge
from graph import Graph

class Kruskal:
	def __init__(self, g):
			self.graph = Graph()
			self.graph = g
			self.parents = {} # Parents dict
			self.depth = {} # Depth dict

	def make_set(self):
		for i in range(0, self.graph.size):
			self.parents[i] = i
			self.depth[i] = 1

	def find(self, val):
		if self.parents[val] == val:
			return val
		self.parents[val] = self.find(self.parents[val])
		return self.parents[val]

	def union(self, val1, val2):
		val1 = self.find(val1)
		val2 = self.find(val2)

		if val1 == val2:
			return
		if self.depth[val1] > self.depth[val2]:
			self.parents[val] = val1
		elif self.depth[val1] == self.depth[val2]:
			self.parents[val1] = val2
			self.depth[val1] += 1
		else:
			self.parents[val1] = val2

	def algorithm(self):
		self.make_set()
		self.graph.sort()

		MSTList = []
		MSTWeight = 0
		
		for edge in self.graph.graph:
			root1 = self.find(edge.start)
			root2 = self.find(edge.end)

			if root1 != root2:
				self.union(root1, root2)
				MSTWeight += edge.weight
		
		print('MST tree:')
		for k, v in self.parents.items():
			if k != v:
				print(f'{k}->{v}')
		print(f'MST weight: {MSTWeight}')
