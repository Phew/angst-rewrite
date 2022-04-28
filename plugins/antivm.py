import ctypes

class AntiVM():
	def __init__(self):
		self.vm = False
		self.inVM()

	def ram_check(self):
		class MemoryStatus(ctypes.Structure):
			_fields_ = [
				("dwLength", ctypes.c_ulong),
				("dwMemoryLoad", ctypes.c_ulong),
				("ullTotalPhys", ctypes.c_ulonglong),
				("ullAvailPhys", ctypes.c_ulonglong),
				("ullTotalPageFile", ctypes.c_ulonglong),
				("ullAvailPageFile", ctypes.c_ulonglong),
				("ullTotalVirtual", ctypes.c_ulonglong),
				("ullAvailVirtual", ctypes.c_ulonglong),
				("sullAvailExtendedVirtual", ctypes.c_ulonglong),
			]
		m = MemoryStatus()
		m.dwLength = ctypes.sizeof(m)
		ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
		ram = m.ullTotalPhys/1073741824
		if ram <= 2:
			self.vm = True

	def screen_size(self):
		x = ctypes.windll.user32.GetSystemMetrics(0)
		y = ctypes.windll.user32.GetSystemMetrics(1)
		if x < 800 or y < 600:
			self.vm = True

	def inVM(self):
		self.ram_check()
		self.screen_size()
		return self.vm
