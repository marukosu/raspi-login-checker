#!/usr/bin/env python

import binascii
import nfc

class CardReader:
	def on_connect(self, tag):
		print "   touched"
		self.idm = binascii.hexlify(tag.idm)
		return True

	def read_id(self):
		clf = nfc.ContactlessFrontend('usb')
		try:
			clf.connect(rdwr={'on-connect': self.on_connect})
		finally:
			clf.close()

if __name__ == '__main__':
	reader = CardReader()
	while True:
		print "** waiting for a tag **"
		reader.read_id()
		print "   idm: " + reader.idm
		print "   released"
