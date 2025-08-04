# test_syntaxparser.py
"""
Tests for SyntaxParser module.
"""

import unittest
from syntaxparser import SyntaxParser

class TestSyntaxParser(unittest.TestCase):
    """Test cases for SyntaxParser class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SyntaxParser()
        self.assertIsInstance(instance, SyntaxParser)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SyntaxParser()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
