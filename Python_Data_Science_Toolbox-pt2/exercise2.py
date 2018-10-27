#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:35:27 2018

@author: jaunalivia
"""

import pandas as pd

df = pd.read_csv('world_ind_pop_data.csv')

row_list = list(df.values)

header_list = list(df.columns)

def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values"""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1,list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

list_of_dicts = [lists2dict(header_list,sublist) for sublist in row_list]

df2 = pd.DataFrame(list_of_dicts)

print(df2.head())
