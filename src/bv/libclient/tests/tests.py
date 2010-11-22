import unittest
import sys


test_modules = map(lambda x: "bv.libclient.tests." + x, ['test_trips',])

map(__import__, test_modules)

modules = [ sys.modules[tm] for tm in test_modules ]
suites = [ m.suite() for m in modules ]

import pdb; pdb.set_trace()
suite = unittest.TestSuite(suites)

suite.run(unittest.TestResult())


