import unittest
from Assignment5 import standard_to_metric

class TestConversionUtility(unittest.TestCase):

    def test_standard_to_metric_conversion(self):
        """Verify that inches are accurately converted to millimeters (1 inch = 25.4 mm)"""
        test_standard = [1.0, 2.0, 10.0]
        test_metric = [0.0, 0.0, 0.0]
        
        # Expected outputs: 1*25.4, 2*25.4, 10*25.4
        expected_metric = [25.4, 50.8, 254.0]
        
        standard_to_metric(test_standard, test_metric)
        
        for calculated, expected in zip(test_metric, expected_metric):
            self.assertAlmostEqual(calculated, expected, places=2)

if __name__ == '__main__':
    unittest.main()
