#The message class for building the NTFY message

class Message():
	def __init__(self, message: str, title: str|None=None, priority: str|None=None):
		self.message=message
		self.dict={}
		if title is not None: self.dict["title"]=title
		if priority is not None: self.dict["priority"]=priority