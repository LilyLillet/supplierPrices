import excel_writer
import read_prices


file = "F:\\goods.txt"
r = open(file, encoding="utf-8")

filename = "112"
file2 = "F:\\" + filename + ".txt"

gorb = "F:\\gorb.xlsx"

l = read_prices.get_goods_list_from_prices(file2, filename)
excel_writer.write_to_excel(gorb, l)






