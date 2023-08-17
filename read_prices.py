ip = "iphone"
airPds = "Air Pods max"
aP = "AirPods max"
appleWtch = "apple watch"
aw = "aw"
watch = "watch"
mcbook = "macbook"

dict_columns = {
    'acer': 3,
    'brothers': 4,
    'nikita': 5,
    'tony': 6,
    '112': 7,
}

def clean_string(input_raw_string):
    cyrilic = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
    ascii_chars = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    nums = '123456789'
    alloud = cyrilic + ascii_chars + nums
    clean_str = ''
    for i in input_raw_string:
        if i in alloud:
            clean_str += i
    return clean_str

def get_decoding_report(file):
    report = open(file, encoding="utf-8")
    lst = list()
    for i in report:
        i_decode = clean_string(i)
        if i_decode != "\n":
            lst.append(i_decode)
    return lst


def get_goods_list_from_prices(file, filename):
    provisioner = filename
    l = get_decoding_report(file)
    lst = list()
    for i in l:
        if "актив" in i or "Мятая коробка" in i: continue
        n = i.lower().replace("gb", "")
        f = n.replace("-", "")
        o = f.replace("(2sim)", "")
        m = o.replace("2 sim", "")
        p = m.replace("2sim", "")
        x = p.replace("tb", "")
        y = x.replace("rfb", "")
        b = y.replace("2021", "")
        q = b.replace("2022", "")
        gg = q.replace("2022", "")
        z = gg.replace(".", "")
        if "s/m" in z or "m/l" in z or "s8" in z or "se2" in z:
            st = z.replace("mm", "")
            sm = st.replace("s/m", "")
            ml = sm.replace("m/l", "")
            brackets = ml.replace("()", "")
            arr_for_check = brackets.split()
            check = len(arr_for_check)
            if check < 3: continue
            if "se2" in z:
                ind = brackets.index("se2") + 3
                stfrom = brackets[ind:]
                arr = stfrom.split()
                ln = len(arr)
                length = arr[0]
                color = arr[1]
                size = ""
                if length == str("40"):
                    size = "s/m"
                elif length == str("44"):
                    size = "m/l"
                if ln == 3:
                    lst.append(str(dict_columns.get(provisioner)) + "Умные часы Apple Watch SE 2 (2022) " + length + "mm " + color + " " + size + " " + arr[2])
                elif ln == 4:
                    lst.append(str(dict_columns.get(provisioner)) + "Умные часы Apple Watch SE 2 (2022) " + length + "mm " + color + " " + size + " " + arr[3])
            if "s8" in z or "8" in z:
                ind = 0
                if "8" in z:
                    ind = brackets.find("8") + 1
                elif "s8" in z:
                    ind = brackets.index("s8") + 2
                stfrom = brackets[ind:]
                arr = stfrom.split()
                ln = len(arr)
                if ln < 2: continue
                length = arr[0]
                color = arr[1]
                if color == "grey" or color == "black" or color == "gray":
                    color = "midnight"
                size = ""
                if length == str("41"):
                    size = "s/m"
                elif length == str("45"):
                    size = "m/l"
                if ln == 3:
                    lst.append(str(dict_columns.get(provisioner)) + "Умные часы Apple Watch Series 8 " + length + "mm " + color + " " + size + " " + arr[2])
                elif ln == 4:
                    lst.append(str(dict_columns.get(provisioner)) + "Умные часы Apple Watch Series 8 " + length + "mm " + color + " " + size + " " + arr[3])
        elif airPds.lower() in z or aP.lower() in z:
            r = z.replace(airPds.lower(), "")
            c = r.replace(aP.lower(), "")
            a = c.split()
            ln = len(a)
            color = a[0]
            if color == "grey":
                color = "black"
            elif color == "white":
                color = "silver"
            if ln == 2:
                lst.append(str(dict_columns.get(provisioner)) + aP + " " + color + " " + a[1])
            elif ln == 3:
                lst.append(str(dict_columns.get(provisioner)) + aP + " " + color + " " + a[2])
        elif "wi" in z or "lte" in z:
            connection = "wi-fi"
            fllrepl = ""
            if "wi" in z:
                frepl = z.replace("wi", "")
                srepl = frepl.replace("fi", "")
                trepl = srepl.replace("wifi", "")
                fllrepl = trepl
            elif "lte" in z:
                connection = "wi-fi + cellular"
                srepl = z.replace("lte", "")
                fllrepl = srepl
            if " 5 " in fllrepl:
                ind = fllrepl.index(" 5 ") + 2
                stfrom = fllrepl[ind:]
                arr = stfrom.split()
                color = arr[1]
                if color == "gray" or color == "grey" or color == "black":
                    color = "space grey"
                ln = len(arr)
                if ln == 3:
                    lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad Air 5 (2022) 10,9\" " + connection + " " + arr[0] + "Gb " + color + " " + arr[2])
                elif ln == 4:
                    lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad Air 5 (2022) 10,9\" " + connection + " " + arr[0] + "Gb " + color + " " + arr[3])
            elif " 9 " in fllrepl:
                ind = fllrepl.index(" 9 ") + 2
                stfrom = fllrepl[ind:]
                arr = stfrom.split()
                ln = len(arr)
                if ln < 2: continue
                color = arr[1]
                if color == "gray" or color == "grey":
                    color = "space grey"
                elif color == "white":
                    color = "silver"
                ln = len(arr)
                if ln == 3:
                    lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10,2\" " + arr[0] + "Gb " + connection + " 9-е поколение " + color + " " + arr[2])
                elif ln == 4:
                    lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10,2\" " + arr[0] + "Gb " + connection + " 9-е поколение " + color + " " + arr[3])
            elif " 10 " in fllrepl:
                ind = fllrepl.index(" 10 ") + 3
                stfrom = fllrepl[ind:]
                arr = stfrom.split()
                ln = len(arr)
                if ln < 2: continue
                color = arr[1]
                if color == "white":
                    color = "silver"
                if ln == 3:
                    lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10 (2022) " + connection + " 10,9\" " + arr[0] + "gb " + color + " " + arr[2])
                elif ln == 4:
                    lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10 (2022) " + connection + " 10,9\" " + arr[0] + "gb " + color + " " + arr[3])
            elif " 11 " in fllrepl or " 12 " in fllrepl or " 129 " in fllrepl:
                trdrepl = fllrepl.replace("m2", "")
                fthrepl = trdrepl.replace("pro", "")
                fifthrepl = fthrepl.replace("()", "")
                sxrepl = fifthrepl.replace("ipad", "")
                ind = 0
                if " 11 " in fllrepl:
                    ind = sxrepl.index(" 11 ") + 3
                elif " 12 " in fllrepl:
                    ind = sxrepl.index(" 12 ") + 3
                elif " 129 " in fllrepl:
                    ind = sxrepl.index(" 129 ") + 4
                stfrom = sxrepl[ind:]
                arr = stfrom.split()
                ln = len(arr)
                if ln < 2: continue
                color = arr[1]
                if color == "white":
                    color = "silver"
                elif color == "black" or color == "gray" or color == "grey":
                    color = "space grey"
                size = "gb"
                if arr[0] == str("1") or arr[0] == str("2"):
                    size = "tb"
                memory = arr[0] + size
                if " 11 " in fllrepl:
                    if ln == 3:
                        lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 11 (2022) " + connection + " " + memory + " " + color + " " + arr[2])
                    elif ln == 4:
                        lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 11 (2022) " + connection + " " + memory + " " + color + " " + arr[3])
                elif " 12 " in fllrepl or " 129 " in fllrepl:
                    if ln == 3:
                        lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 12 12,9' (2022) " + memory + " " + connection + " " + color + " " + arr[2])
                    elif ln == 4:
                        lst.append(str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 12 12,9' (2022) " + memory + " " + connection + " " + color + " " + arr[3])
        elif ip in i or i.startswith("11") or i.startswith("12") or i.startswith("13") or i.startswith(
                "14") or i.lower().startswith("se"):
            s = z.split()
            ln = len(s)
            size = "GB"
            if ln < 3: continue
            if s[2].lower() == "max":
                color = s[4]
                if color == "spgrey":
                    color = "black"
                elif color == "white":
                    color = "silver"
                if s[3] == str("1") or s[3] == str("2"):
                    size = "TB"
                if ln == 6:
                    lst.append(
                        str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + s[2] + " " + str(
                            s[3]) + size + " " + color + " " + str(s[5]))
                else:
                    lst.append(
                        str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + s[2] + " " + str(
                            s[3]) + size + " " + color + " " + str(s[6]))
            elif s[1].lower() == "pro":
                color = s[3]
                if color == "spgrey":
                    color = "black"
                elif color == "white":
                    color = "silver"
                if s[2] == str("1") or s[2] == str("2"): size = "TB"
                if ln == 5:
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[4]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif "se" in i.lower():
                if "40" in i or "44" in i: continue
                if ln == 4:
                    color = s[2]
                    if color == "white":
                        color = "starlight"
                    elif color == "midnight":
                        color = "black"
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + str(
                        s[1]) + size + " " + color + " " + str(s[3]))
                else:
                    color = s[3]
                    if color == "white":
                        color = "starlight"
                    elif color == "midnight":
                        color = "black"
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + str(s[1]) + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif s[1].lower() == "mini":
                color = s[3]
                if color == "midnight":
                    color = "black"
                elif color == "silver" or color == "starlight":
                    color = "white"
                if ln == 5:
                    if s[2] == str("1") or s[2] == str("2"): size = "TB"
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[4]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif s[1].lower() == "plus":
                if s[2] == str("1") or s[2] == str("2"): size = "TB"
                color = s[3]
                if color == "white":
                    color = "starlight"
                elif color == "black":
                    color = "midnight"
                if ln == 5:
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[4]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif s[0].startswith("1"):
                color = s[2]
                if s[0] == "13" or s[0] == "14":
                    if color == "black":
                        color = "midnight"
                    elif color == "white" or color == "silver":
                        color = "starlight"
                if ln == 4:
                    if s[1] == str("1") or s[1] == str("2"): size = "TB"
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + str(
                        s[1]) + size + " " + color + " " + str(s[3]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + ip + " " + s[0] + " " + str(
                        s[1]) + size + " " + color + " " + str(s[4]))
        elif mcbook in z or "air 13" in z or "air pro 13" in z or "air 15" in z:
            frep = z.replace("(", "")
            srep = frep.replace(")", "")
            arr = srep.split()
            model = ""
            price = ""
            for characteristic in arr:
                if characteristic.startswith("m"):
                    if len(characteristic) == 5:
                        model = characteristic
                if characteristic.startswith("1") or characteristic.startswith("2") or characteristic.startswith("3") or characteristic.startswith("4") or characteristic.startswith("5"):
                    if len(characteristic) == 6:
                        price = characteristic
            if len(model) == 5 and len(price) == 6:
                lst.append(str(dict_columns.get(provisioner)) + model + " " + price)
    return lst

