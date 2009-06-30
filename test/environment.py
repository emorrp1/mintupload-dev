#!/usr/bin/env python
def getMintUpload():
	return _getMint("mintUpload")

def getMintUploadCore():
	return _getMint("mintUploadCore")

def _getMint(mintModule):
	import os
	import sys
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option("-p", "--path", dest="basepath", default="", help="relative PATH from the parent directory to the root mintUpload directory. default is empty: the scripts use the parent directory", metavar="PATH")
	(options, args) = parser.parse_args()

	# to import mintUpload, we need to add the root directory of mintUpload to sys.path so the import can find mintUpload
	# this script expects to find mintUpload in the parent directory of this script.
	# for development, its possible to alter the path with the -p parameter if this project is NOT located in the mintUpload root directory (which is the default for development)
	path = os.path.abspath(__file__).rsplit('/',2)[0] + '/' +options.basepath
	sys.path.append(path)
	print "looking for %s in %s ..." %(mintModule, path),
	try:
		exec "import %s as modul"%mintModule
	except ImportError, e:
		print "FAIL"
		print "ImportError: %s. Maybe specify a PATH?" %e
		sys.exit(-1)
	else: 
		print "ok"
		return modul

