import unittest

from Quik import Quik

class TestSetSingulars(unittest.TestCase):
    def setUp(self):
        Quik.set_singulars({})

    def test_1(self):
        # Tests if anything works
        TESTING_DICT = {'a': 'A'}
        Quik.set_singulars(TESTING_DICT)
        self.assertEqual(TESTING_DICT, Quik.get_singulars(), msg="Abcd")

    def test_2(self):
        # Tests if Quik.set_singulars() doesn't accept non-strings
        TESTING_DICT = {'1': 1}
        with self.assertRaises(AttributeError) as ctx:
            Quik.set_singulars(TESTING_DICT)

        self.assertTrue('non-string' in str(ctx.exception))

    def test_3(self):
        # Tests if Quik.set_singulars() doesn't accept non-dicts
        TESTING_LIST = [3, 4, 8]
        with self.assertRaises(AttributeError) as ctx:
            Quik.set_singulars(TESTING_LIST)

        self.assertTrue('requires a dict' in str(ctx.exception))

class TestParseSingulars(unittest.TestCase):
    def test_1(self):
        # Tests if singular parsing works
        TEST_SINGULARS = {
            'a': 'A',
            '420': 'Weed'
        }

        Quik.set_singulars(TEST_SINGULARS) 
        self.assertEqual(Quik.parse_singulars(
            'Lorem ipsum doloret sit {a}met. {420}'),
            'Lorem ipsum doloret sit Amet. Weed')
