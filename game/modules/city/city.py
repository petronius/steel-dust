import citydata

class City(self):
	def __init__(self, name=None):
    
		if self.name is None:
			self.name = citydata.get_random_city_name()