# test_arweaveperm.py
"""
Tests for ArweavePerm module.
"""

import unittest
from arweaveperm import ArweavePerm

class TestArweavePerm(unittest.TestCase):
    """Test cases for ArweavePerm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArweavePerm()
        self.assertIsInstance(instance, ArweavePerm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArweavePerm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
