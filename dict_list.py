import pandas as pd 
import numpy as np
import json 

class DictList(list):

    def __init__(self, *args):
        super().__init__(*args)


    def __getitem__(self, index):
   
        if isinstance(index, tuple):
            list_filter = index[0]
            dict_filter = index[1]
            row_filtered = super().__getitem__(list_filter)
        elif isinstance(index, slice) or isinstance(index, int):
            list_filter= index
            dict_filter = None
            row_filtered = super().__getitem__(list_filter)
        elif isinstance(index, str):
            dict_filter = index
            row_filtered = self

        elif isinstance(index, list) and  isinstance(index[0], str) :
            list_filter = None
            dict_filter = index
            row_filtered = self

        elif isinstance(index, list) and  isinstance(index[0], int) :#We are filtering with a boolean list of dicts
            row_filtered = [row for row, row_boolean in zip(self, index) if row_boolean]
            dict_filter = None
       
        if dict_filter and isinstance(row_filtered, dict):
            col_filtered = row_filtered[dict_filter]

        elif dict_filter and isinstance(row_filtered, list):
            col_filtered = DictList([{key : value for key, value in row.items() if key == dict_filter or key in dict_filter} for row in row_filtered])
        elif isinstance(row_filtered, dict):
            col_filtered = row_filtered
        else:
            col_filtered = DictList(row_filtered)
        return col_filtered

    def __str__(self):
        return json.dumps(self, indent= 1)

    def __setitem__(self, key, value):
        if isinstance(value, list):
            for row, value_to_add in zip(self, value):
                row[key] = value_to_add
        else :
            for row in self:
                row[key] = value
   
    def map(self, f):
        return DictList([f(row) for row in self])


    #OBTENIR LA SHAPE
    def __lt__(self, y):

        return [sum([value < y for value in row.values()]) for row in self]