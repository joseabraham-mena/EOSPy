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


class vanderWaals:

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

    def parameters(self,compound_list):
        r'''
        Calculates the vdWaals parameters a and b for the compound(s) of interest
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
            
            a = (27*(R**2)*(Tc**2))/(64*Pc)
            b = (R*Tc)/(8*Pc)

            inner_dict['a'] = a
            inner_dict['b'] = b

            output_dict[key] = copy.deepcopy(inner_dict)



        return(output_dict)

    def temperature(self,compound_list,pressure,moles,volume):
        r'''
        Calculates temperature for a compound given its pressure (Pa) and volume (m3)
        
        parameters: compound,pressure,volume

        returns: temperature in kelvin
        '''

        compound_data = self.get_data(compound_list)
        compound_parameters = self.parameters(compound_list)

        R = 8.31416
        P = pressure
        V = volume
        n = moles

        inner_dict = {}
        output_dict = {}

        for key in compound_parameters:

            a = float(compound_parameters[key]['a'])
            b = float(compound_parameters[key]['b'])

            T = ((P + a*(n/V)**2)*((V/n)-b))/R

            inner_dict['Temperature'] = T

            output_dict[key] = copy.deepcopy(inner_dict)

        return(output_dict)

    def pressure(self,compound_list,temperature,moles,volume):
        r'''
        Calculates pressure (Pa) for a compound, or a list of compoound given its temperature (K)
        volume (m3), and moles.

        parameters: compound(s),temperature,volume,moles
        
        returns: pressure in Pascals
        '''

        compound_data = self.get_data(compound_list)
        compound_parameters = self.parameters(compound_list)

        R = 8.31416
        T = temperature
        V = volume
        n = moles

        inner_dict = {}
        output_dict = {}

        for key in compound_parameters:

            a = float(compound_parameters[key]['a'])
            b = float(compound_parameters[key]['b'])

            P = (R*T)/((V/n)-b) - (a/((V/n)**2))

            inner_dict['Pressure'] = P

            output_dict[key] = copy.deepcopy(inner_dict)

        return(output_dict)

    # Need to work on solution for Volume

    #def volume(self,compound_list,temperature,moles,pressure):
    #    r'''
    #    Calculates volume(m3) for a compound, or a list of compoound given its temperature (K)
    #    pressure (Pa), and moles.

    #    parameters: compound(s),temperature,volume,moles
        
    #    returns: pressure in Pascals
    #    '''

    #    compound_data = self.get_data(compound_list)
    #    compound_parameters = self.parameters(compound_list)

    #    R = 8.31416
    #    T = temperature
    #    P = pressure
    #    n = moles

    #    tau = np.linspace(-0.5,1.5,201)

    #    inner_dict = {}
    #    output_dict = {}

    #    for key in compound_parameters:

    #        a = float(compound_parameters[key]['a'])
    #        b = float(compound_parameters[key]['b'])

    #        func = lambda V : (R*T) - (P + a/((V/n)**2))*((V/n)-b)
    #        V = np.linspace(-0.5,1.5,201)

    #        plt.plot(V,func(V))
    #        plt.xlabel("V")
    #        plt.ylabel("expression value")
    #        plt.grid()
    #        plt.show()

    #        V = fsolve(func,0)

    #        inner_dict['Volume'] = V

    #        output_dict[key] = copy.deepcopy(inner_dict)

    #    return(output_dict)


 


