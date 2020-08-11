import unittest

class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def test_abc(self):
        print("abc")

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()