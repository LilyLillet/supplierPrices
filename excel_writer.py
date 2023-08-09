import re

import pandas
import openpyxl

import read_prices


def write_to_excel(file_path, lst):
    gg = pandas.read_excel(file_path, sheet_name='1')
    data = gg.iloc[0:]
    for row in data.iterrows():
        good = str(row[1]['iPhone 11'])
        n = good.lower()
        for i in lst:
            g = i.split()
            col_value = g[0]
            col = read_prices.dict_columns.get(col_value)
            t = i.replace(col_value + " ", "")
            ln = len(g)
            price = g[ln - 1]
            c = t.replace(" " + price, "")
            o = c.lower()
            if o in n:
                gg.at[row, col] = price

