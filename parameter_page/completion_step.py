import os 

def write_into(obj):
	print('write_into: Entered')
	file_build = open('current_build.h','w+')
	file_build.write('First Parameter = ' + obj["First_Parameter"] + '\n')
	file_build.write('Second Parameter = ' + obj["Second_Parameter"] + '\n')
	file_build.write('Third Parameter = ' + obj["Third_Parameter"] + '\n')