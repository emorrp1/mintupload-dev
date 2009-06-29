#!/usr/bin/env python

"""doctest utilising test and guitest for mintUpload"""

import unittest
import doctest
import gtk.gdk
from guitest.gtktest import GtkTestCase, guistate, setUp, tearDown
from guitest.utils import mainloop_handler

def doctest_defaultService():
	"""Checks the default Service

	Check the free space script:
		>>> import urllib
		>>> filehandle = urllib.urlopen("http://files.mint-space.com/getfreespace.php")
		>>> text = filehandle.read()

	Do we get a response
		>>> type(text) is str
		True

	Parse/split the response. We expect 2 integer, seperated with a '/'
		>>> splits = text.split('/')
		>>> len(splits)
		2

	Check if available space is a sane output
		>>> type(splits[0]) is int
		True
	
	Check if max space is a sane output
		>>> type(splits[1]) is int
		True
"""

def test_suite():
    # Note: import and use setUp_param instead of setUp if you need to specify
    # custom overrides or logging hooks.  See DoctestHelper.setUp_param().
    return doctest.DocTestSuite(setUp=setUp, tearDown=tearDown)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
