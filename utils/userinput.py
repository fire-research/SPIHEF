import os
import datetime


def process_user_input(inp):

	print(inp)
	Real_time=False
	Retrospective=False
	config_list=[]

	for i in inp:
		if ('Mode_Real_Time' in i):
			if (i[16:] == 'T'):
				Real_time=True
				print("Running in Real time")
				config_list.append('Real_time')

		elif ('Mode_Retrospective' in i):
			if (i[20:] == 'T'):
				Retrospective=True
				print("Running in Retrospective Mode")
				config_list.append('Retrospective Mode')				


		if (Real_time==True):
			if ('NGFS_Feature_Files_Real_Time_Dir' in i):
				NGFS_Feature_Files_Dir  = i[33:]
				config_list.append(NGFS_Feature_Files_Dir)
				date_string=datetime.date.today()
				print(type(date_string))
				if (date_string.day < 10):
					day_string='0'+str(date_string.day)
				config_list.append(str(date_string.year)+'_'+str(date_string.month)+'_'+str(day_string))


		elif (Retrospective==True):
			if ('NGFS_Feature_Files_Retrospective_Dir' in i):
				NGFS_Feature_Files_Dir = i[38:]
				config_list.append(NGFS_Feature_Files_Dir)

			elif ('Start_Date' in i):
				Date=i[11:]
				print(Date)
				config_list.append(Date)

	return config_list



