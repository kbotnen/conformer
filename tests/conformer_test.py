import unittest

import sys
sys.path.append('../')
from conformer import Conformer
 
class ConformerTestClass(unittest.TestCase): 
  def setUp(self):
    self.conformer = Conformer()
  def test_conformer_add_method_return_correct_result(self):
    result = self.conformer.add(2, 2)
    self.assertEqual(4, result)
  def main():
    unittest.main()
    
def main():
    unittest.main()

#We can run our test by issuing: python numpyrunner_test.py
#If we have nosetests available we can issue: nosetests numpyrunner_test.py -sv
if __name__ == "__main__":
    main()
