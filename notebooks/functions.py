# Add all the imports needed by the functions in the project here
#================================================================
#
#================================================================

# Remember to modify your functions to use the template shown below

def function_name(input1: data_type1, input2: data_type2,..., opt_arg: data_type_opt= default_value) -> output_data_type:
	"""
	Add a description of what the function does

	Arguments:
	---------
	input1: data_type and which information should contain
	input2: data_type and which information should contain
	opt_arg: data_type and which information should contain

	Outputs:
	-------
	data_type and which information will contain
	"""
	
	# Your function code here

	
	return opuput


# Importar librerías y cargar datos
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/patriciaviladomiurecio/Desktop/Ironhack/week4/project/first_project/data/raw/Sleep_health_and_lifestyle_dataset.csv")
sleep_df = pd.read_csv(df, encoding='ISO-8859-1')
sleep_df

# Estandarizar nombres de columnas
sleep_df.columns = (
    sleep_df.columns
      .str.lower()
      .str.normalize('NFKD')        # quita acentos
      .str.encode('ascii', errors='ignore')
      .str.decode('utf-8')
      .str.replace(' ', '_')
      .str.replace('[^0-9a-zA-Z_]', '')
)


