#!/usr/bin/env python
import sys
import binascii
# Based on https://github.com/offensive-security/kali-nethunter/blob/master/utils/files/modules/keyseed.py

## Numbers
#"\x30": "\\x00\\x00\\x00\\x27\\x00\\x00\\x00\\x00",
#"\x31": "\\x00\\x00\\x00\\x1e\\x00\\x00\\x00\\x00",
#"\x32": "\\x00\\x00\\x00\\x1f\\x00\\x00\\x00\\x00",
#"\x33": "\\x00\\x00\\x00\\x20\\x00\\x00\\x00\\x00",
#"\x34": "\\x00\\x00\\x00\\x21\\x00\\x00\\x00\\x00",
#"\x35": "\\x00\\x00\\x00\\x22\\x00\\x00\\x00\\x00",
#"\x36": "\\x00\\x00\\x00\\x23\\x00\\x00\\x00\\x00",
#"\x37": "\\x00\\x00\\x00\\x24\\x00\\x00\\x00\\x00",
#"\x38": "\\x00\\x00\\x00\\x25\\x00\\x00\\x00\\x00",
#"\x39": "\\x00\\x00\\x00\\x26\\x00\\x00\\x00\\x00",

dict_us = {
	"a": "\\x00\\x00\\x04\\x00\\x00\\x00\\x00\\x00",
	"b": "\\x00\\x00\\x05\\x00\\x00\\x00\\x00\\x00",
	"c": "\\x00\\x00\\x06\\x00\\x00\\x00\\x00\\x00",
	"d": "\\x00\\x00\\x07\\x00\\x00\\x00\\x00\\x00",
	"e": "\\x00\\x00\\x08\\x00\\x00\\x00\\x00\\x00",
	"f": "\\x00\\x00\\x09\\x00\\x00\\x00\\x00\\x00",
	"g": "\\x00\\x00\\x0a\\x00\\x00\\x00\\x00\\x00",
	"h": "\\x00\\x00\\x0b\\x00\\x00\\x00\\x00\\x00",
	"i": "\\x00\\x00\\x0c\\x00\\x00\\x00\\x00\\x00",
	"j": "\\x00\\x00\\x0d\\x00\\x00\\x00\\x00\\x00",
	"k": "\\x00\\x00\\x0e\\x00\\x00\\x00\\x00\\x00",
	"l": "\\x00\\x00\\x0f\\x00\\x00\\x00\\x00\\x00",
	"m": "\\x00\\x00\\x10\\x00\\x00\\x00\\x00\\x00",
	"n": "\\x00\\x00\\x11\\x00\\x00\\x00\\x00\\x00",
	"o": "\\x00\\x00\\x12\\x00\\x00\\x00\\x00\\x00",
	"p": "\\x00\\x00\\x13\\x00\\x00\\x00\\x00\\x00",
	"q": "\\x00\\x00\\x14\\x00\\x00\\x00\\x00\\x00",
	"r": "\\x00\\x00\\x15\\x00\\x00\\x00\\x00\\x00",
	"s": "\\x00\\x00\\x16\\x00\\x00\\x00\\x00\\x00",
	"t": "\\x00\\x00\\x17\\x00\\x00\\x00\\x00\\x00",
	"u": "\\x00\\x00\\x18\\x00\\x00\\x00\\x00\\x00",
	"v": "\\x00\\x00\\x19\\x00\\x00\\x00\\x00\\x00",
	"w": "\\x00\\x00\\x1a\\x00\\x00\\x00\\x00\\x00",
	"x": "\\x00\\x00\\x1b\\x00\\x00\\x00\\x00\\x00",
	"y": "\\x00\\x00\\x1c\\x00\\x00\\x00\\x00\\x00",
	"z": "\\x00\\x00\\x1d\\x00\\x00\\x00\\x00\\x00",
	".": "\\x00\\x00\\x00\\x37\\x00\\x00\\x00\\x00",
	"/": "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00",
	":": "\\x20\\x00\\x00\\x33\\x00\\x00\\x00\\x00",
	";": "\\x00\\x00\\x00\\x33\\x00\\x00\\x00\\x00",
	"<": "\\x20\\x00\\x00\\x36\\x00\\x00\\x00\\x00",
	"=": "\\x00\\x00\\x00\\x2e\\x00\\x00\\x00\\x00",
	">": "\\x20\\x00\\x00\\x37\\x00\\x00\\x00\\x00",
	"?": "\\x20\\x00\\x00\\x38\\x00\\x00\\x00\\x00",
	"@": "\\x20\\x00\\x00\\x1f\\x00\\x00\\x00\\x00",
}
cmwn = "\\x80\\x00\\x00\\x2c\\x00\\x00\\x00\\x00" 
enter = "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00"
stop = "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00"

file = sys.argv[1]
f = open('attack', 'w')

def cmd_space():
	f.write(binascii.unhexlify(cmwn.replace('\\x','')))
	f.write(binascii.unhexlify(stop.replace('\\x','')))

def press_string():
	d = open(file, 'r')
	for i in d.readlines():
		i = i.replace('\n','')
		if i == '<enter>':
			press_enter()
		if i == '<cmwn>':
			cmd_space()
		else:
			for s in i:
				for a,b in dict_us.items():
					if s == a:
						f.write(binascii.unhexlify(b.replace('\\x','')))			
						f.write(binascii.unhexlify(stop.replace('\\x','')))

def press_enter():
	f.write(binascii.unhexlify(enter.replace('\\x','')))
	f.write(binascii.unhexlify(stop.replace('\\x','')))

press_string()

