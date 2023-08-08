import pandas
import openpyxl

import read_prices


file = "F:\\goods.txt"
r = open(file, encoding="utf-8")

filename = "112"
file2 = "F:\\" + filename + ".txt"

l = read_prices.get_goods_list_from_prices(file2, filename)

for m in r:
    n = m.lower()
    for i in l:
        s = i[1:]
        r = s.split()
        ln = len(r)
        price = r[ln - 1]
        c = s.replace(" " + price, "")
        o = c.lower()
        if o in n:
            print(s)


#gg = pandas.read_excel(file, sheet_name='1')