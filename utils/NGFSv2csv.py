import pandas as pd
import numpy as np
import glob
import os


def get_file_list(path):

	# csv files in the path
	print('looking in path')
	print(path) 
	#files = glob.glob(path + "/NGFS_FIRE_EVENTS_GOES-17_ABI_Full-Disk*.csv")
	#NGFS_FIRE_EVENTS_INTERNAL
	#files = glob.glob(path + "/NGFS_FIRE_EVENTS_INTERNAL*.csv") 
	#files = glob.glob(path + "/NGFS_FIRE_DETECTIONS_GOES-17_ABI_Full*.csv")
	files=glob.glob(path + "/NGFS_FIRE_FEATURES_GOES-17_ABI_Full*.csv")
	
	print(len(files))
	print(files)	
	return files




def get_file_list_mod(path):

	#For 2024 runs (Adityak(07/02/2024)
	#cmd='ls NGFS_FIRE_DETECTIONS_GOES-18_ABI_CONUS_2024_06*csv > /home/adityak/Fire_Initiative_Project/ngfs_csv_file_list.txt'
	#For Park fire (Adityak (07/30/2024))
	cmd='ls NGFS_FEATURES_GOES-18_ABI_CONUS_2024_07_2*csv > /home/adityak/Fire_Initiative_Project/ngfs_csv_file_list.txt'

	#Commenting for 2020 runs (Adityak, 07/02/2024)
	#cmd = 'ls NGFS_FIRE_FEATURES_GOES-17_ABI_Full-Disk_*csv > /home/adityak/Fire_Initiative_Project/ngfs_csv_file_list.txt'
	#cmd = 'ls NGFS_FIRE_FEATURES_GOES-17_ABI_CONUS_2019*csv > /home/adityak/Fire_Initiative_Project/ngfs_csv_file_list.txt' 
	filelist = 'ngfs_csv_file_list.txt'
	curr_dir=os.getcwd()
	os.chdir(path)
	print(os.getcwd())	
	os.system(cmd)
	os.chdir('/home/adityak/Fire_Initiative_Project/')
	return filelist





def combine_files_mod(files,path):

	#os.chdir(path)


	with open(files) as f:

		lines = f.readlines()
		print(type(lines))
        	#lines = lines.strip()
		print(lines)	


	final_file_list=[]
	final_df = pd.DataFrame()	

	os.chdir(path)

	for x in lines:


		filename_temp=x.strip()
		#filename_temp=x.strip()

		final_file_list.append(filename_temp)
		print('now reading file')
		print(filename_temp)
        	
		df = pd.read_csv(filename_temp,on_bad_lines='skip')

		final_df = pd.concat([final_df, df], ignore_index=True)


	return final_df




def combine_files(files):

	# checking all the csv files in the  
	# specified path 
	data_frame = pd.DataFrame() 
	content = []
	
	for filename in files: 
    
    
		df = pd.read_csv(filename, index_col=None) 
		content.append(df) 
  
	# converting content to data frame 
	data_frame = pd.concat(content) 
	return data_frame




def get_col_names(df):

	col_list=[]
	for col in df.columns:
		col_list.append(col)

	return col_list




def group_cols(df,cols_list):

	df_gr=df.groupby(cols_list)
	return df_gr
		


def plot_ts(df):

	pass