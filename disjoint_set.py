

class DisjointSet(object):

	def __init__(self,items):

		self._disjoint_set = list()

		if items:
			for item in set(items):
				self._disjoint_set.append([item])

	def _get_index(self,item):
		for s in self._disjoint_set:
			for _item in s:
				if _item == item:
					return self._disjoint_set.index(s)
		return None

	def find(self,item):
		for s in self._disjoint_set:
			if item in s:
				return s
		return None

	def find_set(self,item):

		s = self._get_index(item)

		return s+1 if s is not None else None 

	def union(self,item1,item2):
		i = self._get_index(item1)
		j = self._get_index(item2)

		if i != j:
			self._disjoint_set[i] += self._disjoint_set[j]
			del self._disjoint_set[j]
	
	def get(self):
		return self._disjoint_set