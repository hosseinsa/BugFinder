import unittest

import sys
sys.path.insert(0, r'C:\Users\hossein\Desktop\SW Developer Test')

import os
import codecs
from Code.BugFinder import extract_data, bug_finder, boundry_bug_Counter


#_______________________________________________________________________________
path = os.getcwd()
valid_path =  path + '\\valid_bug'
error_path =  path + '\\error_bug'
wrong_path =  path + '\\wrong_bug'
#bugempty = os.path.join(path, 'Empty_txt.txt')

bugpath = os.path.join(path, 'bug.txt')
landscape_path = os.path.join(path, 'landscape.txt')

line_list = extract_data(landscape_path).split('\n')
pattern_ = extract_data(bugpath).split('\n')

#readfile = lambda bugpath: codecs.open(bugpath, 'r').read().split('\n')
#print [readfile(text) for text in [bugpath]]

txt_valid = [valid_path + '\\' + TxtTestCase for TxtTestCase in os.listdir(valid_path)]
txt_error = [error_path + '\\' + TxtTestCase for TxtTestCase in os.listdir(error_path)]
txt_wrong = [wrong_path + '\\' + TxtTestCase for TxtTestCase in os.listdir(wrong_path)]

print txt_error
#-------------------------------------------------------------------------------

class TestExtractDara(unittest.TestCase):

	#Override the setUp() class method to set up initial state for all test methods.
	def setUp(self):
		txt_to_test = txt_valid + txt_error
		for f in txt_to_test:
			self.file = open(f, "r")
			pass


	#Override the tearDown() class method to perform final cleanup after all test methods complete.
	def tearDown(self):
		self.file.close()
		pass

	def test_extract_data_IsString(self):
		txt_to_test = txt_wrong + txt_error + txt_valid
		for bug in txt_to_test:
			self.assertEqual(type(extract_data(bug)), str)

	def test_extract_data_CorrectText(self):
		txt_to_test = txt_error + txt_valid
		for bug_path in txt_to_test:
			in_file = open(bug_path, "r")
			text = in_file.read()
			in_file.close()
			self.assertEqual(extract_data(bug_path), text)

	def test_NoneExsistingPath(self):
		for txt in txt_wrong:
			with self.assertRaises(IOError):
				extract_data(txt)

	def test_errorPath(self):
		for n in [20, [], {'index':'Test'}, {set}]:
			with self.assertRaises(TypeError):
				extract_data(n)


class TestBugFinder(unittest.TestCase):
	def setUp(self):
		self.counter = 0
		for i in range(len(line_list)):
			self.counter+= bug_finder(line_list[i:i+ len(pattern_)], pattern_)

	def tearDown(self):
		pass 

	 
	def testBugFinderOutput_CountInt(self):
		self.assertEqual(self.counter, 3)

	def testBugFinderOutput_Count_Not_int(self):
		if line_list[0].count(pattern_[0]) == 0:
		 	self.assertRaises(IOError)

	def testBugFinderOutput_if_find_pattern(self):
		for n, element in enumerate(pattern_):
			if element != line_list[0:len(pattern_)][n]:
				self.assertRaises(IOError)

	

class TestBoundries(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def testBoundries_BugCounter(self):
		test_counter = 0
		test_counter += boundry_bug_Counter(line_list[12:12+len(pattern_)], pattern_)
		self.assertEqual(test_counter, 0)



#This allows us to run all of the test code just by running the file.
if __name__ == '__main__':
    unittest.main()