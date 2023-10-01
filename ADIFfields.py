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
ID_FIELD_NAME   = 0
ID_DATA_TYPE    = 1
ID_ENUMERATION  = 2
ID_DESCRIPTION  = 3
NUM_TABLE_ITEMS = 4

# csv filename
OUT_FILENAME = 'ADIFfields.csv'
OUT_FILENAME_FIELD_ONLY = 'ADIFfields_only.csv'

class ADIF_fields:
    '''class ADIFfields

        ADIFfields class handles ADIF Field Headers.
        Args:
            None
        Returns:
            None
    '''
    def __init__(self):
        # ADIFfields.csv is existing?
        if os.path.isfile(OUT_FILENAME):
            print(f'{OUT_FILENAME} is existing.')
            self.df_all = pd.read_csv(OUT_FILENAME)
        else:
            self.fetch_fields()
            self.df_all.to_csv(OUT_FILENAME)

    def fetch_fields(self):
        '''fetch field table data from adif.org'''
        try:
            response = requests.get(URL, timeout=(3.0, 7.5))
        except requests.exceptions.Timeout:
            pass
        soup = BeautifulSoup(response.content, 'html.parser')

        # extract ADIF field list table, class=fieldtable, second one
        table = soup.find_all('table', {'class':'fieldtable'})[1]
        table_td = table.find_all('td')
        all_data_list = []
        _i = 0
        for field in table_td:
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

                all_data_list.append( [tmp_field,
                                       tmp_data_type,
                                       tmp_enum,
                                       tmp_description.strip()] )

            _i += 1


        self.df_all = pd.DataFrame(all_data_list, columns=TABLE_INDEX)


    def get_all_fields(self) -> pd.DataFrame:
        '''get_all_fields returns all of field data'''
        return self.df_all

    def get_fields(self) -> pd.Series:
        '''get_fields returns DataFrame'''
        return self.df_all[ TABLE_INDEX[ID_FIELD_NAME] ]

    def get_field_list(self) -> list:
        '''get_field_list returns list of fields'''
        out_list = []
        for each_field_name in self.df_all[ TABLE_INDEX[ID_FIELD_NAME] ]:
            out_list.append(each_field_name)
        return out_list

    @classmethod
    def get_table_index(cls) -> list:
        '''get_table_index

            get_table_index, @classmethod, returns list of index: TABLE_INDEX.

            Args:
                None
            Returns:
                list: list of index: TABLE_INDEX
        '''
        return TABLE_INDEX

    def save_all_fields(self, csvfilepath=OUT_FILENAME):
        '''save df_all to file
            Args:
                csvfilepath (str): csv file path,
        '''
        if os.path.isfile(csvfilepath):
            print(f'{csvfilepath} is existing.')
        else:
            try:
                self.df_all.to_csv(csvfilepath)
            except IOError:
                print(f'cannot save file: {csvfilepath}')

    def save_fields(self, csvfilepath=OUT_FILENAME_FIELD_ONLY):
        '''save df_all['Field Name] to csv file
            Args:
                csvfilepath (str): to save pd.Series of 'Field Name' 
        '''
        if os.path.isfile(csvfilepath):
            print(f'{csvfilepath} is existing.')
        else:
            try:
                self.df_all[ TABLE_INDEX[ID_FIELD_NAME] ].to_csv(csvfilepath)
            except IOError:
                print(f'cannot save file: {csvfilepath}')

    def print_all(self):
        '''just print `df_all` on console'''
        return print(self.df_all)


def main():
    '''main()

        main function to test ADIFfields() class methods
    '''
    adif_fields = ADIF_fields()

    print(adif_fields.get_all_fields())
    print(adif_fields.get_fields())
    print(adif_fields.get_field_list())
    print(adif_fields.get_table_index())

    adif_fields.save_all_fields()
    adif_fields.save_fields()


if __name__ == '__main__':
    main()
