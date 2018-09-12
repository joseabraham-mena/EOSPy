import csv
import copy 
import math
import collections 
import numpy as np
import pandas as pd

from math import *
from tabulate import tabulate
from collections import OrderedDict 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


class ReducedVariables:

    def __init__(self,name):
        self.name = name

    def get_data(self,compound_list):
        r'''
        Given the compound, this function retrieves its critical properties and error for each.
        :return: critical properties of compound(s)
        '''
        data_dict = []
        output_data = {}
        headers = ['CAS ID','Pc','Pc_Error','Tc','Tc_Error','Vc','Vc_Error']
        database_dir = r"C:\Users\jam66\source\repos\EOSPy\Databases\Database.csv"
        
        with open(database_dir,encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                    data_dict.append(row)

        for c in compound_list:
            for dictionary in data_dict:
                if dictionary['Compound'] == c:
                    inner_dict = {}
                    output_data[c] = inner_dict
                    inner_dict['CAS_ID'] = dictionary['CAS ID']
                    inner_dict['Tc'] = dictionary['Tc']
                    inner_dict['Tc_Error'] = dictionary['Tc_Error']
                    inner_dict['Pc'] = dictionary['Pc']
                    inner_dict['Pc_Error'] = dictionary['Pc_Error']
                    inner_dict['Vc'] = dictionary['Vc']
                    inner_dict['Vc_Error'] = dictionary['Vc_error']
    
        return(output_data)

    def tabulate_data(self,data_dictionary):
        table = []
        headers = ['Compound']

        for item in data_dictionary:

            inner_table = []
            inner_table.append(item)

            for key,value in data_dictionary[item].items():
                headers.append(key)
                inner_table.append(value)
     
            table.append(inner_table)

        print('Units are Kelvin,Pascals,and cubic meters/mol')
        print(tabulate(table,headers))

    def parameters(self,compound_list,temperature,pressure,volume):
        r'''
        This function calculates the vdWaals parameters a and b for the compound(s) of interest
        :param compound: specify compound(s)
        :return: van der Waals parameters
        '''
        compound_data = self.get_data(compound_list)
        parameters = []
        R = 8.31416

        inner_dict = {}
        output_dict = {}

        for key in compound_data:
            Tc = float(compound_data[key]['Tc'])
            Pc = float(compound_data[key]['Pc'])
            Vc = float(compound_data[key]['Vc'])
            
            T = temperature
            P = pressure 
            V = volume

            Tr = T/Tc
            Pr = P/Pc
            Vr = V/Vc

            inner_dict['Tr'] = Tr
            inner_dict['Pr'] = Pr
            inner_dict['Vr'] = Vr

            output_dict[key] = copy.deepcopy(inner_dict)

        return(output_dict)

    def temperature(self,compound_list,pressure,volume):
        r''' Calcualtes the temperature of a compound or list of compounds using reduced vanderWaals
        :param compound: specify compound(s),pressure, and volume
        :return: temperature and reduced temperature for each compound
        '''
        compound_data = self.get_data(compound_list)
        parameters = []
        R = 8.31416

        inner_dict = {}
        output_dict = {}

        for key in compound_data:
            Tc = float(compound_data[key]['Tc'])
            Pc = float(compound_data[key]['Pc'])
            Vc = float(compound_data[key]['Vc'])
            
            P = pressure 
            V = volume

            Pr = P/Pc
            Vr = V/Vc
            
            Tr = ((Pr + (3/(Vr**2)))*(Vr - 1/3))/(8/3)
            T = Tr*Tc

            inner_dict['Temperature Reduced'] = Tr
            inner_dict['Temperature'] = T

            output_dict[key] = copy.deepcopy(inner_dict)

        return(output_dict)

    def pressure(self,compound_list,temperature,volume):
        r''' Calcualtes the temperature of a compound or list of compounds using reduced vanderWaals
        :param compound: specify compound(s),pressure, and volume
        :return: temperature and reduced temperature for each compound
        '''
        compound_data = self.get_data(compound_list)
        parameters = []
        R = 8.31416

        inner_dict = {}
        output_dict = {}

        for key in compound_data:
            Tc = float(compound_data[key]['Tc'])
            Pc = float(compound_data[key]['Pc'])
            Vc = float(compound_data[key]['Vc'])
            
            T = temperature 
            V = volume

            Tr = T/Tc
            Vr = V/Vc
            
            Pr = ((8/3*Tr)/(Vr-1/3)) - 3/(Vr**2)
            P = Pr*Tc

            inner_dict['Pressure Reduced'] = Pr
            inner_dict['Pressure'] = P

            output_dict[key] = copy.deepcopy(inner_dict)

        return(output_dict)
    