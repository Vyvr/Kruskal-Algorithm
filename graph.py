from edge import Edge

class Graph:
	def __init__(self):
		self.graph = []
		self.size = 0

	def insert(self, e):
		if e not in self.graph:
			self.graph.append(e)
			self.size += 1

	def sort(self):
		self.graph.sort(key=lambda Edge: Edge.weight)

	def remove_edge(self, start, end):
		for e in self.graph:
			if e.start == start and e.end == end:
				self.graph.remove(e)
				return

	def __repr__(self):
		return repr(self.graph)