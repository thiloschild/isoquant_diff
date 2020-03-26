import configparser
import pandas as pd
import sys


def get_data(file):

	if file.endswith(".ini"):
		data = get_data_ini(file)
	elif file.endswith(".xlsx"):
		data = get_data_excel(file)
	else:
		print("Please use and .ini or .xlsx file!")

	return data

def validate_file(file):

	if file.endswith(".ini"):
		valid_file = True
	elif file.endswith(".xlsx"):
		valid_file = True
	else:
		valid_file = False

	return valid_file


def get_data_ini(file):

	config = configparser.ConfigParser()
	with open(file, 'r') as f:
	    config_string = '[dummy_section]\n' + f.read()
	config.read_string(config_string)
	data = config.items('dummy_section')
	# turn list into dict
	data_dict = {item[0]: item[1] for item in data}
	return data_dict


def get_data_excel(file):

	csv = pd.ExcelFile(file)
	df = pd.read_excel(csv, 'config')
	df = df[['Unnamed: 3', 'Unnamed: 4']]
	df = df.iloc[2:]
	df = df.set_index("Unnamed: 3")
	data_dict = df.to_dict()
	data_dict = data_dict["Unnamed: 4"]
	data_dict = to_lowercase(data_dict)
	return data_dict


def check_for_numbers(data):

	for x in data:
		data[x] = conv2float(data[x])
	return data


def create_list_of_parameters(dict1,dict2):

	parameters = []
	for x in dict1:
		parameters.append(x)
	for x in dict2:
		if x in parameters:
			pass
		else:
			parameters.append(x)
	for y in parameters:
		if y in dict1:
			pass
		else:
			dict1[y] = "NotSet"
		if y in dict2:
			pass
		else:
			dict2[y] = "NotSet"
	return parameters


def diff_config(file1,file2,report_unique=False):

	if validate_file(file1) and validate_file(file2) == True:

		dict1 = get_data(file1)
		dict2 = get_data(file2)
		dict1 = check_for_numbers(dict1)
		dict2 = check_for_numbers(dict2)

		parameters = create_list_of_parameters(dict1, dict2)
		df = pd.DataFrame(columns=['parameters', file1, file2])

	
		for x in parameters:
			new_row = {'parameters': x, file1: dict1[x], file2: dict2[x]}
			row_df = pd.DataFrame([new_row])
			df = pd.concat([df, row_df], ignore_index=True)
			df = df[df[file1] != df[file2]]
			if report_unique == True:
				pass
			else:
				if dict1[x]  == "NotSet" or dict2[x] == "NotSet":
					df = df[:-1]
		return df
	else:
		print("Please use and .ini or .xlsx file!")



def conv2float(s):
	try:
		float(s)
		return float(s)
	except ValueError:
		return s

def to_lowercase(data):

	data = {str(key).lower() : (transform(value) if isinstance(value, dict)
			 else value) for key, value in data.items()}
	return data


#########################################################################
file1 = sys.argv[1]
file2 = sys.argv[2]

df = diff_config(file1,file2)

print(df)

# html = df.to_html()

# text_file = open("diff_between_"+file1+"_"+file2+".html", "w")
# text_file.write(html)
# text_file.close()