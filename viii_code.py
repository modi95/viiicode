import sys
import os

# Given a path to a file, opens that file and creates an array of strings.
# Each entry in the array is a line in the file. Line trails are stripped.
#
# @param src_file_path: path of the file to arrrayize
# @return array created from input file.
def file_to_array(src_file_path):
	src_file = open(src_file_path)
	lines = []
	for line in src_file:
		lines.append(line.strip())
	return lines

def main():
	src = file_to_array(sys.argv[1])
	for line in src: print line
	return

if __name__ == "__main__":
	main()
