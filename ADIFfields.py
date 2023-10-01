#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:56:41 2023

@author: JS2IIU-MH
"""
import os

import requests
from bs4 import BeautifulSoup

import pandas as pd

# ADIF FIELD TABLE
# URL = 'https://adif.org/adif'
URL = 'http://adif.org/314/ADIF_314.htm'
# III.C.1.b QSO Fields
# 0: Field Name
# 1: Data Type
# 2: Enumeration
# 3: Description
TABLE_INDEX = ['Field Name', 'Data Type', 'Enumeration', 'Description']
ID_FIELD_NAME = 0
ID_DATA_TYPE = 1
ID_ENUMERATION = 2
ID_DESCRIPTION = 3
NUM_TABLE_ITEMS = 4

# csv filename
OUT_FILENAME = 'ADIFfields.csv'
OUT_FILENAME_FIELD_ONLY = 'ADIFfields_only.csv'

class ADIFfields:
    def __init__(self):
        # ADIFfields.csv is existing?
        if os.path.isfile(OUT_FILENAME):
            print('{} is existing.'.format(OUT_FILENAME))
            self.df_all = pd.read_csv(OUT_FILENAME)
        else:
            self.fetch_fields()
            self.df_all.to_csv(OUT_FILENAME)

    # fetch field table data from adif.org
    def fetch_fields(self):
        # fetch ADIF document web
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # extract ADIF field list table, class=fieldtable, second one
        table = soup.find_all('table', {'class':'fieldtable'})[1]
        tr = table.find_all('td')
        all_data_list = []
        _i = 0
        for field in tr:
            if _i % NUM_TABLE_ITEMS == ID_FIELD_NAME:
                # Field Name
                tmp_field = field.get_text()
            elif _i % NUM_TABLE_ITEMS == ID_DATA_TYPE:
                # Data Type
                tmp_data_type = field.get_text()
            elif _i % NUM_TABLE_ITEMS == ID_ENUMERATION:
                # Enumeration
                tmp_enum = field.get_text()
            elif _i % NUM_TABLE_ITEMS == ID_DESCRIPTION:
                # Description
                tmp_description = field.get_text()
                lines = tmp_description.splitlines()
                tmp_description = ''.join(lines)
                
                all_data_list.append( [tmp_field, tmp_data_type, tmp_enum, tmp_description.strip()] )
            
            _i += 1
        
        
        self.df_all = pd.DataFrame(all_data_list, columns=TABLE_INDEX)

    # get_all_fields returns all of field data
    def get_all_fields(self) -> pd.DataFrame:
        return self.df_all

    # get_fields returns DataFrame
    def get_fields(self) -> pd.Series:
        return self.df_all[ TABLE_INDEX[ID_FIELD_NAME] ]
    
    
    # get_field_list returns list of fields
    def get_field_list(self) -> list:
        out_list = []
        for s in self.df_all[ TABLE_INDEX[ID_FIELD_NAME] ]:
            out_list.append(s)
        return out_list
    
    
    # get_table_index returns list of index: TABLE_INDEX
    @classmethod
    def get_table_index(cls) -> list:
        return TABLE_INDEX
    
    # save df_all to file
    def save_all_fields(self, csvfilepath=OUT_FILENAME):
        if os.path.isfile(csvfilepath):
            print('{} is existing.'.format(csvfilepath))
        else:
            try:
                self.df_all.to_csv(csvfilepath)
            except:
                print('cannot save file: {}'.format(csvfilepath))
            
    # get_fields returns DataFrame
    def save_fields(self, csvfilepath=OUT_FILENAME_FIELD_ONLY):
        if os.path.isfile(csvfilepath):
            print('{} is existing.'.format(csvfilepath))
        else:
            try:
                self.df_all[ TABLE_INDEX[ID_FIELD_NAME] ].to_csv(csvfilepath)
            except:
                print('cannot save file: {}'.format(csvfilepath))    

    # print DataFrame
    def print_all(self):
        return print(self.df_all)


def main():
    
    af = ADIFfields()
    
    print(af.get_all_fields())
    print(af.get_fields())
    print(af.get_field_list())
    print(af.get_table_index())
    
    af.save_all_fields()
    af.save_fields()
    

if __name__ == '__main__':
    main()
    