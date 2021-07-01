class Edge:
	"""
	Module represents single edge in graph.
	Contains start, end apex and weight of the edge.
	"""
	def __init__(self, start, end, weight):
		self.start = start
		self.end = end
		self.weight = weight

	def __repr__(self):
		return repr(print(f'{self.start}, {self.end}     weight: {self.weight}'))