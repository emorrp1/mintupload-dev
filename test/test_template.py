#!/usr/bin/env python

import unittest
import gtk.gdk
from guitest.gtktest import GtkTestCase, guistate, setUp, tearDown
from guitest.utils import mainloop_handler

class TestRemplate(unittest.TestCase):
	'''Template for unittests'''

	def testFeature1(self):
		'''Check Feature 1'''
		pass

	def testFeature2(self):
		'''Check Feature 2'''
		pass


if __name__ == '__main__':
	import mintUploadTesting
	mintUpload = mintUploadTesting.getMintUpload()
	mintUploadCore = mintUploadTesting.getMintUploadCore()
	print "--- start tests---"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestDefaultService)
	unittest.TextTestRunner(verbosity=2).run(suite)
