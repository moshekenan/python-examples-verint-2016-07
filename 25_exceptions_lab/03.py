import unittest
import os
import tempfile
import shutil

class InvalidImageExt(Exception):
    def __init__(self, msg):
        super(InvalidImageExt, self).__init__(msg)

class ImageFile:
    def __init__(self, name):
        self.path = name
        file_extension = name.split(".")[-1]
        print file_extension
        if file_extension != 'png':
            raise InvalidImageExt("png should be a valid file extension") 

        open(self.path, 'a').close()


class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()