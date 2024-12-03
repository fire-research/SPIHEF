import os
import pandas






def read_ascii_file(path, fname):

	
	full_file_path=path+'/'+fname
	f=open(full_file_path)
	lines = f.readlines()
	final_list=[]
	for x in lines:
		final_list.append(x.strip())

	return final_list
