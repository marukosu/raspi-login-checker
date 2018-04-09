#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import binascii
import nfc
import json
import requests
import time

class CardReader:
	def __init__(self):
		post_url = os.environ.get('POST_URL') 
		print(post_url)
		if post_url is None:
			print('POST_URL(environment variable) is undefined', file=sys.stderr)
			sys.exit()
		self.post_url = post_url

	def on_connect(self, tag):
		print('   touched')
		self.idm = binascii.hexlify(tag.idm)
		self.post_data()
		return True
	
	def post_data(self):
		data = {
			'idm': self.idm,
			'ts': time.time()
		}
		print('   request data: ' + str(data))
		response = requests.post(self.post_url, json=data)
		print('   response status code: ' + str(response.status_code))

	def read_id(self):
		clf = nfc.ContactlessFrontend('usb')
		try:
			clf.connect(rdwr={'on-connect': self.on_connect})
		finally:
			clf.close()


if __name__ == '__main__':
	reader = CardReader()
	while True:
		print('** waiting for a tag **')
		reader.read_id()
		print('   released')
