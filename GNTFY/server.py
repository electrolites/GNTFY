from .message import Message
import httpx

class Server:
	def __init__(self, topic: str, url: str="https://ntfy.sh"):
		self.topic=topic
		self.url=url

	def send(self, message: Message):
		httpx.post(f"{self.url}/{self.topic}", data=message.message, headers=message.dict)