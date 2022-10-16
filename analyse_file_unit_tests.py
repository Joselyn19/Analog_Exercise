'''
Unit tests for analyse_file.py
'''
import unittest
from analyse_file import AnalyseFile


class AnalyseFileUnitTests(unittest.TestCase):
    '''
    Unit tests for analyse_file.py
    '''
    def test_invalid_drt(self):
        '''
        test case: Invalid directory
        '''
        analyse = AnalyseFile()
        dirct, exten = 'ff', ''
        self.assertEqual(analyse.line_count(dirct, exten), (0, 0, 0.00))

    def test_no_such_file(self):
        '''
        test case: no target extension in directory
        '''
        analyse = AnalyseFile()
        dirct, exten = './test_directory', '.cpp'
        self.assertEqual(analyse.line_count(dirct, exten), (0, 0, 0.00))

    def test_no_drt_in_current_drt(self):
        '''
        test case: no other directory in the current directory
        '''
        analyse = AnalyseFile()
        dirct, exten = './test_directory/sub_directory1', '.txt'
        self.assertEqual(analyse.line_count(dirct, exten), (1, 1, 6.00))

    def test_have_drt_in_current_drt(self):
        '''
        test case: has directories in the current directory
        '''
        analyse = AnalyseFile()
        dirct, exten = './test_directory', '.txt'
        self.assertEqual(analyse.line_count(dirct, exten), (4, 4, 7.25))

    def test_extension_md(self):
        '''
        test case: has directories in the current directory, extension .md
        '''
        analyse = AnalyseFile()
        dirct, exten = './test_directory', '.md'
        self.assertEqual(analyse.line_count(dirct, exten), (3, 3, 12.33))

    def test_extension_py(self):
        '''
        test case: has directories in the current directory, extension .py
        '''
        analyse = AnalyseFile()
        dirct, exten = './test_directory', '.py'
        self.assertEqual(analyse.line_count(dirct, exten), (1, 1, 4.00))

if __name__ == '__main__':
    unittest.main()
