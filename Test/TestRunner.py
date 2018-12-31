import unittest
from Tester import TestExtractData, TestBugFinder, TestBoundries

ExtractData = unittest.TestLoader().loadTestsFromTestCase(TestExtractData)
BugFinder = unittest.TestLoader().loadTestsFromTestCase(TestBugFinder)
Boundries = unittest.TestLoader().loadTestsFromTestCase(TestBoundries)

Suit_finder = unittest.TestSuite([ExtractData,
								BugFinder,
								Boundries,
								])

Results = unittest.TextTestRunner(verbosity = 2).run(Suit_finder)