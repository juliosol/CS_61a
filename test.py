'''
from operator import add, sub, mul, truediv

def inform_all_except(source, message, constraints):
	"""Inform all constraints of the message, except source."""
	for c in constraints:
		if c != source:
			c[message]()

def connector(name=None):
	"""A connector between constraints"""
	informant = None
	constraints = []
	def set_value(source, value):
		nonlocal informant
		val = connector['val']
		if val is None:
			informant, connector['val'] = source, value
			if name is not None:
				print(name, '=', value)
			inform_all_except(source, 'new_val', constraints)
		else:
			if val != value:
				print('Contradiction detected:', val, 'vs', value)
	def forget_value(source):
		nonlocal informant
		if informant == source:
			informant, connector['val'] = None, None
			if name is not None:
				print(name, 'is forgotten')
			inform_all_except(source, 'forget', constraints)
	connector = {'val': None,
				 'set_val': set_value,
				 'forget': forget_value,
				 'has_value': lambda: connector['val'] is not None,
				 'connect': lambda source: constraints.append(source)}
	return connector

def adder(a,b,c):
	"""The constraint that a + b = c"""
	return make_ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a,b,c):
	"""The contraint that a*b = c"""
	return make_ternary_constraint(a,b,c, mul, truediv, truediv)

def constant(connector, value):
	"""The constraint that connector = value"""
	constraint = {}
	connector['set_val'](constraint, value)
	return constraint

def make_ternary_constraint(a, b, c, ab, ca, cb):
	"""The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a"""
	def new_value():
		av, bv, cv = [connector['has_value']() for connector in (a,b,c)]
		if av and bv:
			c['set_val'](constraint, ab(a['val'], b['val']))
		elif av and cv:
			b['set_val'](constraint, ca(c['val'], a['val']))	
		elif bv and cv:
			a['set_val'](constraint, cb(c['val'], b['val']))
	def forget_value():
		for connector in (a,b,c):
			connector['forget'](constraint)
	constraint = {'new_val':new_value, 'forget':forget_value}
	for connector in (a,b,c):
		connector['connect'](constraint)
	return constraint


def converter(c,f):
	"""Connect c to f with constraints to convert from Celsius to Fahrenheit"""
	u,v,w,x,y = [connector() for _ in range(5)]
	multiplier(c,w,u)
	multiplier(v,x,u)
	adder(v,y,f)
	constant(w, 9)
	constant(x, 5)
	constant(y, 32)


celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

converter(celsius, fahrenheit)


def mario_number(level):
	if level[0] == 'P' or len(level) == 0:
		return 0
	elif len(level) <= 2:
		return 1
	else:
		return mario_number(level[1:]) + mario_number(level[2:])

def mario_number_alt(level):
	if str(level)[0] == 1 or len(str(level)) == 0:
		return 0
	elif len(str(level)) <= 2:
		return 1
	else:
		return mario_number_alt(int(str(level)[1:])) + mario_number_alt(int(str(level)[2:]))
'''

# Tree constructor

def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

# Selectors 
def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return not branches(tree)

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def tree_max(t):
	return max([label(t)] + [label(p) for p in branches(t)])

def height(t):
	if is_leaf(t):
		return 0
	else:
		return 1 + height(branches(t))

def square_tree(t):
	if is_leaf(t):
		return tree(label(t) ** 2)
	else:
		bs = [square_tree(b) for b in branches(t)]
		return tree(label(t) ** 2, bs)

def find_path(tree, x):
	if label(tree) == x:
		return [label(tree)]
	for b in branches(tree):
		path = find_path(b,x)
		if path:
			return [label(tree)] + path

def prune(t,k):
	if k == 0:
		return [label(t)]
	for b in branches(t):
		 
		  [label(t)] + prune(b,k-1)


