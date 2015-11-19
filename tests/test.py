import unittest
import sys
import os.path
sys.path.append('../libs')
from utils import *

class TestUtilsFunctions(unittest.TestCase):
    
    def test_is_number(self):
        for i in range(0,9):
            self.assertTrue(is_number(str(i)))
        self.assertFalse(is_number(','))
        self.assertFalse(is_number(' '))
        self.assertFalse(is_number('a'))

    def test_argv_resolver(self):
        os.chdir("..")
        self.assertEquals(argv_resolver([0,]), ('pi1000.txt', 'pi1000.mid') )
        self.assertEquals(argv_resolver([0,'pi1000.txt']), ('pi1000.txt', 'pi1000.mid') )
        self.assertFalse(argv_resolver([0,'test.txt'])[0] )
        self.assertFalse(argv_resolver([0,'test.txt_', 'test.mid'])[0] )
        self.assertFalse(argv_resolver([0,'test.txt', 'test.mid_'])[0] )
        os.chdir("./tests")
        self.assertEquals(argv_resolver([])[0], False )

suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilsFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
