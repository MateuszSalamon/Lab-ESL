import unittest
from myhdl import *
import os

from Cezar import Cezar



class TestCezar(unittest.TestCase)

    def testOriginalCezar(selfself):

        mode = Signal(0)
        message = [Signal(intbv(0)[127:]) for x in range(127)]
        key = Signal(intbv(126)[7:].signed())


if __name__ == '__main__':
    unittest.main(verbosity=2)