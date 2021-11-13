#!/usr/bin/python3
"""
Module test_file_storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.user import User

class TestFileStorage(unittest.TestCase):
    """
    Unit tests FileStorage engine
    """

    def test_no_private_var_access(self):
        """
        Should not access private variables
        """
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
            FileStorage.__objects

"""
    def test_method_new(self):
        s = FileStorage()
        dic = s.all()
        user = User()
        user.id = 123
        user.name = "Nehe"
        s.new(user)
        u_id = str(user.id)
        key = str(user.__class__.__name__) + "." + u_id
        self.assertIsNotNone(dic[key])
"""
