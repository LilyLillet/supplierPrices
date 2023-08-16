import excel_writer
import read_prices

l = list()

filename = "acer"
file = "F:\\" + filename + ".txt"
acer_price = read_prices.get_goods_list_from_prices(file, filename)
for i in acer_price:
    l.append(i)


filename2 = "brothers"
file2 = "F:\\" + filename2 + ".txt"
brothers_price = read_prices.get_goods_list_from_prices(file2, filename2)
for i in brothers_price:
    l.append(i)


filename3 = "nikita"
file3 = "F:\\" + filename3 + ".txt"
nikita_price = read_prices.get_goods_list_from_prices(file3, filename3)
for i in nikita_price:
    l.append(i)


filename4 = "tony"
file4 = "F:\\" + filename4 + ".txt"
tony_price = read_prices.get_goods_list_from_prices(file4, filename4)
for i in tony_price:
    l.append(i)


filename5 = "112"
file5 = "F:\\" + filename5 + ".txt"
stg_price = read_prices.get_goods_list_from_prices(file5, filename5)
for i in stg_price:
    l.append(i)


gorb = "F:\\gorb.xlsx"

excel_writer.write_to_excel(l, gorb)






