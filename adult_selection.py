class full_replacement:
	def select(adults, children):
		return children
        
class overproduction:
	def select(adults, children):
		return children.get_most_fit(adults.size())
		
class generational_mixing:
	def select(adults, children):
		combined = adults.combine(children)
		return combined.get_most_fit(adults.size())
