class selection_protocol(object):
	litter_size = None

class full_replacement(selection_protocol):
	def __init__(this, popsize):
		litter_size = popsize

	def select(this, adults, children):
		return children
		
class overproduction(selection_protocol):
	def __init__(this, _):
		litter_size = int(input("Input litter size: "))

	def select(this, adults, children):
		return children.get_most_fit(adults.size())
		
class generational_mixing(selection_protocol):
	def __init__(this, _):
		litter_size = int(input("Input litter size: "))

	def select(this, adults, children):
		combined = adults.combine(children)
		return combined.get_most_fit(adults.size())

protocols = {"full_replacement":full_replacement, "overproduction":overproduction, "generational_mixing":generational_mixing}
