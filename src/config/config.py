global config

config = {
	
	# details required to login to twitch IRC server
	'server': 'irc.twitch.tv',
	'port': 6667,
	'username': 'KappaPMBot',
        'oauth_password': 'oauth:yjtjj80dna78urwbwh5hqp0j8t0aen', # get this from http://twitchapps.com/tmi/
	
	# channel to join
	'channels': ['#hotform'],

	'cron': {
		'#channel_one': {
			'run_cron': False, 	# set this to false if you want don't want to run the cronjob but you want to preserve the messages etc
			'run_time': 30, 		# time in seconds
			'cron_messages': [
				'This is channel_one cron message one.',
				'This is channel_one cron message two.'
			]
		}
	},

	# if set to true will display any data received
	'debug': False,

	# if set to true will log all messages from all channels
	# todo
	'log_messages': True,

	# maximum amount of bytes to receive from socket - 1024-4096 recommended
	'socket_buffer_size': 2048
}

