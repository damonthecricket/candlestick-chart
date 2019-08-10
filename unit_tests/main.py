
import unittest

from . import test_axe
from . import test_db
from . import test_model
from . import test_shape


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_axe)   )
suite.addTests( loader.loadTestsFromModule(test_db)    )
suite.addTests( loader.loadTestsFromModule(test_model) )
suite.addTests( loader.loadTestsFromModule(test_shape) )

runner = unittest.TextTestRunner(verbosity = 3)
result = runner.run(suite)