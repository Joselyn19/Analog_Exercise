'''
Script to count file lines in given directory with specific extension
--directory set directory, required
--extension set extension, default .txt
cmd:
python3 line_count_script.py --directory [required]_your_directory_ --extension _your_extension_
'''
import argparse
from analyse_file import AnalyseFile

parser = argparse.ArgumentParser(
    description='count line in given files')
parser.add_argument(
    '--directory', required=True, type=str,
    help='set directory, required')
parser.add_argument(
    '--extension', required=False, default='.txt', type=str,
    help='set extension, default .txt')
args = parser.parse_args()


if __name__ == '__main__':
    analyse = AnalyseFile()
    cnt_file, cnt_lines, cnt_avg = analyse.line_count(args.directory, args.extension)
    print("Number of files found: {0}".format(cnt_file))
    print("Total number of lines: {0}".format(cnt_lines))
    print("Average lines per file: {0}".format(cnt_avg))
