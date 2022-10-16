'''
Module analyse_file has following class:
AnalyseFile
'''
import os
import chardet

class AnalyseFile:
    '''
    AnalyseFile Class provides methods to analyse files
    '''
    @classmethod
    def get_encoding(cls, file):
        '''
        get the encoding of the file
        '''
        with open(file, 'rb') as file2:
            return chardet.detect(file2.read())['encoding']

    def line_count(self, direct, exten):
        '''
        Get lines of files in directory with specific extension
        '''
        ## Invalid Directory
        if not os.path.exists(direct):
            print('No such directory!')
            return 0, 0, 0.00

        cnt_file = 0 # number of files found
        cnt_lines = 0 # total number of lines

        # Find All Files By DFS
        def dfs_files(curr_direct):
            nonlocal cnt_file, cnt_lines, exten
            file_list = os.listdir(curr_direct)
            for file in file_list:
                new_direct = curr_direct+'/'+file
                if os.path.isdir(new_direct):
                    dfs_files(new_direct)
                elif os.path.isfile(new_direct):
                    _, suffix = os.path.splitext(file)
                    if suffix == exten:
                        cnt_file += 1
                        encoding = self.get_encoding(new_direct)
                        with open(new_direct, 'r', encoding=encoding) as file2:
                            cnt_lines += len(file2.readlines())

        dfs_files(direct)

        if cnt_file != 0:
            cnt_avg = cnt_lines/cnt_file
        else:
            cnt_avg = 0
        return cnt_file, cnt_file, round(cnt_avg, 2)
