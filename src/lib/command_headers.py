from src.config.config import *

commands = {
	'!testkpm': {
		'limit': 30,
		'return': 'Kappa'
	},
	'!kpm': {
		'limit': 30,
		'argc': 0,
		'return': 'command'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
