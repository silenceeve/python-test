'''
@Time   : 2020/5/8 10:04
@Author : Silence
@File   : TestStringMethods.py
@Version: V1.0.0
'''
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO');

    def test_isupper(self):
        self.assertTrue('FOO'.isupper());
        self.assertFalse('Foo'.isupper());

    def test_split(self):
        s = 'hey Silence';
        self.assertEqual(s.split(),['hey','Silence']);
        with self.assertRaises(TypeError):
            s.split(2);

    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods);
    unittest.TextTestRunner(verbosity=2).run(suite);