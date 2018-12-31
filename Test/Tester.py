import unittest 
import os 
import sys 

sys.path.insert(0, r'C:\Users\hossein\Desktop\SW Developer Test')

from Code.BugFinder import extract_data, bug_finder, boundry_bug_Counter

path = os.getcwd()
bug_path = os.path.join(path, 'bug.txt')
landscapePath = os.path.join(path, 'landscape.txt')

error_path = os.path.join(path, 'error_bug')
valid_path  = os.path.join(path,'valid_bug')
empty_path = os.path.join(path, 'wrong_bug')

ErrorFolder = [error_path + '\\' + TxtFileName for TxtFileName in os.listdir(error_path)]
ValidFolder = [valid_path + '\\' + TxtFileName for TxtFileName in os.listdir(valid_path)]
WrongFolder = [empty_path + '\\' + TxtFileName for TxtFileName in os.listdir(empty_path)]

#----------------------------------------------------------------------------------------
big_list = extract_data(landscapePath).split('\n')
pattern_ = extract_data(bug_path).split('\n')
#----------------------------------------------------------------------------------------



class TestExtractData(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_extractData_str(self):
		for bug in ValidFolder:
			in_file = open(bug, "r")
			text = in_file.read()
			in_file.close()
			self.assertEqual(type(extract_data(bug)), str)
		

	def test_extractData_ErrorPath(self):
		for bug in ErrorFolder:
			with self.assertRaises(IOError):
				extract_data(bug)


	def test_extractData_NonExistingPath(self):
		for bug in WrongFolder:
			with self.assertRaises(IOError):
				extract_data(bug)			

	def test_extractData_WrongPath(self):
		for bug in [20, {}, {'key':'value'}, []]:
			with self.assertRaises(TypeError):
				extract_data(bug)	




class TestBugFinder(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_BugFinder_IsInt(self):
		counter = 0
		counter += bug_finder(big_list[1:1+len(pattern_)], pattern_)
		self.assertEqual(counter, 1)

	def test_BugFinder_Check_if_pattern(self):
		for n, element in enumerate(pattern_):
			if element != big_list[0:len(pattern_)][n]:
				self.assertRaises(IOError)




class TestBoundries(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_boundry_bug_Counter(self):
		counter = 0
		counter += boundry_bug_Counter(big_list[12:12+len(pattern_)], pattern_)
		self.assertEqual(counter, 0)


	def test_boundry_bug_counter_checkPattern(self):
		First_pattern = big_list[0].count(pattern_[0])
		if not First_pattern:
			 self.assertNotEqual(First_pattern, 1, msg=None)

#if __name__ == '__main__':
#	unittest.main()