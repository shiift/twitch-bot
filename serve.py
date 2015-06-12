#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config.config import *
from threading import *


arr_data = { 'arr_lock': Lock(), 'arr_loc': 0, 'kappa_arr': [0 for i in range(60)] }

class timer(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
		self.start()
	def run(self):
		while True:
			global arr_data
			
			time.sleep(5)
			
			arr_data['arr_lock'].acquire()
			if(arr_data['arr_loc'] < 59):
				arr_data['arr_loc'] += 1
			else:
				arr_data['arr_loc'] = 0
			arr_data['kappa_arr'][arr_data['arr_loc']] = 0
			arr_data['arr_lock'].release()

class robot(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
		self.start()
	def run(self):
		global arr_data
		bot = Roboraj(config).run(arr_data)


timer()
robot()
while True:
	pass
