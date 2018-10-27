#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:07:02 2018

@author: jaunalivia
"""

# BRINGING IT ALL TOGETHER

# Dictionary Exercise
feature_names = ['CountryName',
                 'CountryCode',
                 'IndicatorName',
                 'IndicatorCode',
                 'Year',
                 'Value']

row_vals = ['Arab World',
            'ARB',
            'Adolescent fertility rate (births per 1,000 women ages 15-19)',
            'SP.ADO.TFRT',
            '1960',
            '133.56090740552298']

zipped_list = zip(feature_names,row_vals)

rs_dict = dict(zipped_list)

print('Dictionary Exercise output 1:\n')
print(rs_dict)
print('\nDictionary Exercise output 2:\n')
[print(key+': '+value) for key, value in rs_dict.items()]
print('\n')

# Function Exercise
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides 
    the keys and list2 provides the values"""
    
    # Zip lists: zipped_lists
    zipped_lists = zip(list1,list2)
    
    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)
    
    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names,row_vals)

# Print rs_fxn
print('Function Exercise output:\n')
print(rs_fxn)

# List Comprehension Exercise

# Print the first two lists in row_lists
print()

# Turn list of lists into list of dicts: list_of_dicts


# Print the first two dictionaries in list_of_dicts

