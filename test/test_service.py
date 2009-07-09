#!/usr/bin/env python

import unittest
import gtk.gdk
from guitest.gtktest import GtkTestCase, guistate, setUp, tearDown
from guitest.utils import mainloop_handler

class TestDefaultService(unittest.TestCase):
	'''TestCases for the Default mintUpload Service'''

	def testFTPRunning(self):
		'''Check if FTP is Running'''
		from ftplib import FTP
		try:
			ftp = FTP('linuxmint.com')   # connect to host, default port
			ftp.login('sef0i34vppp','F873uioweBV')
		except Exception, e:
			self.fail(e)

	def testHTTPRunning(self):
		'''Check the mint-space server'''
		import urllib2
		try:
			urllib2.urlopen("http://mint-space.com")
		except urllib2.HTTPError, e:
			if e.code == 401:
				self.fail('401: not authorized')
			elif e.code == 403:
				self.fail('403: forbidden')
			elif e.code == 404:
				self.fail('404: not found')
			elif e.code == 503:
				self.fail('503: service unavailable')
			else:
				self.fail('unknown error')

	def testFreeSpaceScript(self):
		'''Check the free space script'''
		import urllib2
		try:
			filehandle = urllib2.urlopen("http://files.mint-space.com/getfreespace.php")
		except urllib2.HTTPError, e:
			if e.code == 401:
				self.fail('401: not authorized')
			elif e.code == 403:
				self.fail('403: forbidden')
			elif e.code == 404:
				self.fail('404: not found')
			elif e.code == 503:
				self.fail('503: service unavailable')
			else:
				self.fail('unknown error')
		else:
			text = filehandle.read()
			#Do we get a response
			self.assertTrue(type(text) is str)

			#Parse/split the response. We expect 2 integer, seperated with a '/'
			splits = text.split('/')
			self.assertEqual(len(splits), 2, "expected only 2 numbers as response")
			splits = map(str.strip,splits)
			#Check if available space and max space is a sane output
			try:
				int(splits[0])
				int(splits[1])
			except ValueError, e:
				self.fail(e)

if __name__ == '__main__':
	print "--- start tests---"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestDefaultService)
	unittest.TextTestRunner(verbosity=2).run(suite)
