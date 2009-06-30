#!/usr/bin/env python

import unittest
import gtk.gdk
from guitest.gtktest import GtkTestCase, guistate, setUp, tearDown
from guitest.utils import mainloop_handler

class TestTemplate(unittest.TestCase):
	'''Template for unittests'''

	def testFeature1(self):
		'''Check Feature 1'''
		pass

	def testFeature2(self):
		'''Check Feature 2'''
		pass


if __name__ == '__main__':
	#import mintUploadTesting

	## aditional CLI Arguments:
	#parser = mintUploadTesting.getOptParser()
	#parser.add_option("-t", "--test", dest="test", default="", help="this is a test option", metavar="PATH")

	## get parsed CLI Options
	#options = mintUploadTesting.getOptions()
	
	##get mintUpload Modules
	#mintUpload = mintUploadTesting.getMintUpload()
	#mintUploadCore = mintUploadTesting.getMintUploadCore()

	print "--- start tests---"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
	unittest.TextTestRunner(verbosity=2).run(suite)
