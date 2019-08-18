
import unittest

from . import test_axe
from . import test_shape


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_axe)   )
suite.addTests( loader.loadTestsFromModule(test_shape) )

runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)