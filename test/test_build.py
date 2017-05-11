from unittest import TestCase


class TestBuild(TestCase):
#check if the  number is not declare
#check if the 0 goes to the last position

    def test_number_is_not_declare(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Success")

        result = build(None)
        self.assertEqual(False,result)

    def test_number_goes_to_last_position(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Success")

        result = build([1,0,0,1])
        self.assertTrue([1,1,0,0],result)