import csv
import copy 
import math
import copy
import collections 
import numpy as np
import pandas as pd

from math import *
from tabulate import tabulate
from collections import OrderedDict 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


class Virial:

	def __init__(self,name):
		self.name = name

	def get_data(self,compound_list):
		r'''
		Given the compound, this function retrieves its critical properties and error for each.
		:return: critical properties of compound(s)
		'''
		data_dict = []
		output_data = {}
		database_dir_1 = r"C:\Users\jam66\source\repos\EOSPy\Databases\VirialCoefficients.csv"
		database_dir_2 = r"C:\Users\jam66\source\repos\EOSPy\Databases\Database.csv"

		with open(database_dir_1,encoding = 'utf-8-sig') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				data_dict.append(row)

		for c in compound_list:
			for dictionary in data_dict:
				if dictionary['Compound'] == c:
					inner_dict = {}

					inner_dict['CAS_ID'] = dictionary['CAS ID']
					inner_dict['b0'] = dictionary['b0']
					inner_dict['b1'] = dictionary['b1']
					inner_dict['b2'] = dictionary['b2']
					inner_dict['b3'] = dictionary['b3']
					inner_dict['c0'] = dictionary['c0']
					inner_dict['c1'] = dictionary['c1']
					inner_dict['c2'] = dictionary['c2']
					inner_dict['c3'] = dictionary['c3']
					inner_dict['f0'] = dictionary['f0']
					inner_dict['f1'] = dictionary['f1'] 

					output_data[c] = copy.deepcopy(inner_dict) 

		return(output_data)

	#def tabulate_data(self,data_dictionary):

	#	table = []
	#	headers = ['Compound']

	#	for item in data_dictionary:

	#		inner_table = []
	#		inner_table.append(item)

	#		for key,value in data_dictionary[item].items():
	#			headers.append(key)
	#			inner_table.append(value)
     
	#		table.append(inner_table)

	#print('Units are Kelvin,Pascals,and cubic meters/mol')
	#print(tabulate(table,headers))

	#def parameters(self,compound_list):
	#	r'''
	#	Calculates the vdWaals parameters a and b for the compound(s) of interest
	#	:param compound: specify compound(s)
	#	:return: van der Waals parameters
	#	'''
	#	compound_data = self.get_data(compound_list)
	#	parameters = []
	#	R = 8.31416

	#	inner_dict = {}
	#	output_dict = {}

	#	for key in compound_data:

	#		Tc = float(compound_data[key]['Tc'])

	#		b0 = float(compound_data[key]['b0'])
	#		b1 = float(compound_data[key]['b1'])
	#		b2 = float(compound_data[key]['b2'])
	#		b3 = float(compound_data[key]['b3'])
	#		c0 = float(compound_data[key]['c0'])
	#		c1 = float(compound_data[key]['c1'])
	#		c2 = float(compound_data[key]['c2'])
	#		c3 = float(compound_data[key]['c3'])
	#		f0 = float(compound_data[key]['f0'])
	#		f1 = float(compound_data[key]['f1'])
            
	#		b = b0 + b1/tr + b2/(tr**2) + b3/(tr**3)
	#		c = c0 + c1/tr + c2/(tr**2) + c3/(tr**3)
	#		f = f0 + f1/tr

	#		inner_dict['a'] = a
	#		inner_dict['b'] = b
	#		inner_dict['c'] = c

	#		output_dict[key] = copy.deepcopy(inner_dict)

	#	return(output_dict)