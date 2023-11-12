from GNTFY import message
import httpx

class Server():
	def __init(self, topic: str, url: str="https://ntfy.sh"):
		self.url=url
		self.topic=topic

	def send(self, message: ntfy.message):
		httpx.post(f"{url}/{topic}", data=message.message, headers=message.headers)