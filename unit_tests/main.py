
import unittest

from . import test_db
from . import test_model


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_db)    )
suite.addTests( loader.loadTestsFromModule(test_model) )

runner = unittest.TextTestRunner(verbosity = 3)
result = runner.run(suite)