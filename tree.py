def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return not branches(tree)

def sum_range(t):
	def helper(t):
		if is_leaf(t):
			return [label(t), label(t)]
		else:
			a = min([helper(branches(t))])
			b = max([helper(branches(t))])
			x = label(t)
			return [b + x, a + x]
	x, y = helper(t)
	return x - y
