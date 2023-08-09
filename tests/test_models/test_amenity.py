#!/usr/bin/python3
""" this class for testing Amenity """
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """ for Check BaseModel """

    def testpep8(self):
        """ for Testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
