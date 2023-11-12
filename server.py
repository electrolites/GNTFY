from GNTFY.message import Message
import httpx

class Server():
	def __init(self, topic: str, url: str="https://ntfy.sh"):
		self.url=url
		self.topic=topic

	def send(self, message: Message):
		httpx.post(f"{url}/{topic}", data=message.message, headers=message.headers)