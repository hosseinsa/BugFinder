#! user/bin/env python
# --coding: ascii--


# FILE HEADER
##
# @file BugFinder.py
# @author Hossein Sarpanah
# @version 1.0.0
# @brief Counting the bugs in a corrupted text file 
# @details Interface class Manages inputs and outputs w/ user.
# Related functions perform tasks specific for extracting bugs
# and corrupted texts from two files bug.txt and landscape.txt
# @note None
# @bug None
# @warning None
# @date 07-01-2018

import os

path = os.getcwd()
bug_path = path + '\\' + 'bug.txt'
document_path = path + '\\' + 'landscape.txt'


def extract_data(path_to_file):
    """
    @brief Reading a file and returning a list of its contents
    @details This function is used to read a text file(here bug.txt and landscape.txt) and to return a list of
    file's content 
    @param path_to_file: The path of files that should be passed in.
    @note Note that open should appear outside of the try. If open itself raises an exception, the file wasn't
    opened and does not need to be closed.
    @return text: List(Of String)
    """
    try:
        in_file = open(path_to_file, "r")
        text = in_file.read()
        in_file.close()
        if text == '':
            return False
    except Exception as exception:
        raise
    return text


def bug_finder(line_list, elements):
    """
    @brief Counting number of bug pattern in a limitted list of the whole landscape.txt file  

    @details According to the definition of this function, it takes n lines each time and looks for the first
    element of bug pattern in the firs line and maintaines index of these elements to find other pattern's
    elements in other lines. At the end compares the available pattern with the found index elements.
    For example, function gets the first 3 lines(lines #0, #1, #2) of landscape and checks how many times '| |'
    is repeated then if its three, checks other two lines for three times to find exact same pattern. Then gets
    a new three lines(#1, #2, #3) and so on.. 

    @param line_list: a list which should be analyzed (has a length equal to the bug pattern)
    @param pattern_: bug pattern
    @return rest: number of bugs
    """
    rest = 0
    starting_point = 0

    for _ in range(line_list[0].count(elements[0])):
        starting_point += line_list[0][starting_point+1:].index(elements[0])+1
        if elements == [line_list[l][starting_point:starting_point + len(elements[l])] for l in range(len(elements))]:
            rest += 1

    return rest


def boundry_bug_Counter(big_list, pattern):
    """
    @brief Defining the boundries for the Large-Scale files
    @details This function limits thoses lines of landscape file which have not any pattern' elements.
    @param big_list a list of all lines in landscape.txt
    @param pattern a list of all lines in bug.txt
    @return: number of bugs
    """
    bugs = 0
    for n, line in enumerate(big_list):
        if pattern[0] in line and len(big_list[n:n+len(pattern)]) == len(pattern):
            bugs += bug_finder(big_list[n:n+len(pattern)], pattern)
#    print 'There are <%s> bugs in your provided documnet!' % bugs
    return bugs


# Making a list of the contents of the bug.txt
extract_bugs = extract_data(bug_path)
pattern = extract_bugs.strip().split('\n')

# Making a list of the contents of the file which should be analyzed(landscape.txt)
corrupted_document = extract_data(document_path)
big_list = corrupted_document.split('\n')

boundry_bug_Counter(big_list, pattern)
