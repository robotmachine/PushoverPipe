#!/usr/bin/python

"""
* Pushover Pipe
* for Python 3
* 
* robotmachine(a)gmail(d)com
* http://github.com/robotmachine/Pushover_Pipe
*
* This program is free software. It comes without any warranty, to
* the extent permitted by applicable law. You can redistribute it
* and/or modify it under the terms of the Do What The Fuck You Want
* To Public License, Version 2, as published by Sam Hocevar. See
* http://sam.zoy.org/wtfpl/COPYING for more details.
"""

""" All of this is built in to Python 3. (No dependencies) """
import os, sys, urllib, http.client, configparser, textwrap, argparse


settings = os.path.expanduser("~/.pushpipe")
config = configparser.ConfigParser()

def main():
	parser = argparse.ArgumentParser(description='Pushover thing', prog='Pushover Pipe')
	parser.add_argument('-u','--user',
		action='store', dest='user', default=None,
		help='User key instead of reading from settings. Requires --token.')
	parser.add_argument('-t','--token',
		action='store', dest='token', default=None,
		help='Token key instead of reading from settings. Requires --user.')
	args = parser.parse_args()
	read_config(token=args.token, user=args.user)

def read_config(token, user):
	if token is None and user is None:
		if os.path.exists(settings):
			config.read(settings)
			token = config['PUSHPIPE']['token']
			user = config['PUSHPIPE']['user']
			message(token, user)
		if not os.path.exists(settings):
			set_config()
	elif token is not None and user is not None:
		message(token, user)

def message(token, user):
	print("API Token: ")
	print(token)
	print("User Key: ")
	print(user)

def set_config():
	print(textwrap.dedent("""
	You will need to create an app 
	in Pushover and provide the token.
	https://pushover.net/apps
	"""))
	token = input("API Token: ")
	print(textwrap.dedent("""
	Your user key is found on your 
	Pushover.net Dashboard	
	https://pushover.net
	"""))
	user = input("User Key: ")
	config ['PUSHPIPE'] = {'token': token,
			       'user': user}		
	with open(settings, 'w') as configfile:
		config.write(configfile)
	message(token, user)

main()
