from GNTFY.message import Message
import httpx

class Server:
	def __init__(self, topic: str, url: str="https://ntfy.sh"):
		self.url=url
		self.topic=topic

	def send(self, message: Message):
		httpx.post(f"{self.url}/{self.topic}", data=message.message, headers=message.headers)