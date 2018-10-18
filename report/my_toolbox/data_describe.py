# -*- coding: utf-8 -*-
'''
This tool provides an easy and quick over view for data. 
It helps user to select null features. 
----------------------------------
This module require install pandas and numpy. 
pip install pandas
pip install numpy
'''


import pandas as pd
import numpy as np


def data_describe(df):
    '''
    ----------------------------------
    'duplicate' column is the number of each feature in data which contain how many different members.
    'is_null' column means whether the feature has null number or not.
    'null_number' means how many null numbers does the feature has.
    ''null_rate(%)' is the persentage show that feature has. Be calculated like: null_number/len(df[feature])
    ----------------------------------
    df: the data frame user want to check.
    '''
#     df.info()
#     df.shape()
#     print(df.isnull().any().sum(), "columns have null number")

    describe = pd.DataFrame()
    _duplicate_num(df, describe)
    _is_null_number(df, describe)
    describe['null_rate(%)'] = describe['null_number']*100/len(df)
    describe['null_rate(%)'] = describe['null_rate(%)'].map(lambda x: ('%.2f')%x)

    return describe
    
    
    
def _duplicate_num(df, describe):
    dup_num = df.apply(lambda x:x.unique().shape[0], axis=0)
    describe['duplicate'] = dup_num
    
    
    
def _is_null_number(df, describe):
    describe['is_null'] = df.isnull().any()
    describe['null_number'] = df.isnull().sum()

    
    
def data_type (describe, default_type_name, data_type_dict):
    '''
    ----------------------------------
    Append a column 'type' behind the table from data_describe(df).
    Put a dictionary on  'data_type_dict'. 
    Beside the item in 'data_type_dict' will be setted as 'default_type_name'.
    ----------------------------------
    describe: This is the pandas dataframe from 'data_describe(df)'.
    default_type_name: The type will be set for the feature beside the item you set in 'data_type_dict'.            
    data_type_dict:  
            Example:  data_type_dict = {'category':['month', 'type'], 'numeric':['price','quantity']}
    '''
    describe['type'] = default_type_name
    for type_name in data_type_dict:
        describe.loc[data_type_dict[type_name],'type'] = type_name
    
    
    
    
# if __name__ == '__main__':

    