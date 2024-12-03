import pandas as pd
from utils import fascii
from utils import userinput
from utils import NGFScsv
import os





def main():


	print("================================================================================")
	print("            Smoke Plume Injection Height Estimation and Forecasting             ")
	print("================================================================================")

	user_input_list=fascii.read_ascii_file(os.getcwd(),'user_input.txt')
	config_list=userinput.process_user_input(user_input_list)
	print(config_list)

	NGFScsv.get_file_list(config_list[1],config_list[2])




if __name__ == "__main__":

	main()











