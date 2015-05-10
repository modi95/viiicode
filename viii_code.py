import sys
import os
from bf_operators import *

bf_ops = ['>', '<', '+', '-', '.', ',', '[', ']' ] #
dataspace = []
instr = 0
ptr = 0

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

def array_to_bfarray(src):
	bf_array = []
	for line in src:
		for ch in line:
			if ch in bf_ops:
				bf_array.append(ch)
	return bf_array

# Given an array of brainfuck operators

def parse_jumps(bf_array):
	bf_jump = [];
	jumpbacks = [];

	for i in range(0, len(bf_array)):

		if (bf_array[i] is '['):
			jumpbacks.append(i)
			bf_jump.append(-1)

		elif (bf_array[i] is ']'):
			if (len(jumpbacks) is 0): exit_error()
			bf_jump.append( jumpbacks.pop() )

		else:
			bf_jump.append(-1)

	if (not len(jumpbacks) is 0):
		exit_error()

	return bf_jump

def execute_on_arrays(bf_operations, bf_control):
	#instr = 0
	#ptr = 0
	global instr
	global ptr
	instr = int(0)
	ptr = int(0)
	dataspace.append(0)
	while (instr < len(bf_operations)):
		execute_decision(bf_operations[instr], bf_control[instr])
		#print (str(dataspace) + " " + str(instr))

	print ("End of instr")

def execute_decision(op, nl):
	global instr
	global ptr
	if ((ptr+1) > len(dataspace)):
		dataspace.append(0)
	
	if (op is '>'):
		ptr += 1

	elif (op is '<'):
		ptr -=1

	elif (op is '+'):
		dataspace[ptr] += 1

	elif (op is '-'):
		dataspace[ptr] -= 1

	elif (op is '.'):
		print chr(dataspace[ptr]),

	elif (op is ','):
		dataspace[ptr] = ord(raw_input("input char:")[0])

	elif (op is '['):
		instr += 1
		return

	elif (op is ']'):
		if (dataspace[ptr] is 0):
			instr += 1
			return
		instr = nl

	instr += 1


def exit_error():
	print ("exit_error")

def main():
	src = file_to_array(sys.argv[1])
	bf_array = array_to_bfarray(src)
	jumps = parse_jumps(bf_array)
	#for i in range(0, len(bf_array)):
		#print ("line " + str(i) + ": \t" + str(bf_array[i]) + " " + str(jumps[i]))
	execute_on_arrays(bf_array, jumps)
	return

if __name__ == "__main__":
	main()