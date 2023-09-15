ip = "iphone"
airPds = "air pods max"
aP = "airpods max"
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
        elif i not in alloud:
            clean_str += " "
    # to don't add goods from China, Taiwan and Hong Kong to list
    if '🇨🇳' in input_raw_string or '🇹🇼' in input_raw_string or '🇭🇰' in input_raw_string:
        clean_str = ""
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
        strng = i.lower()
        # clearing list from all unnecessary characteristics
        if "актив" in strng or "коробка" in strng or "2 sim" in strng or "2sim" in strng or "lz" in strng or "угол" in strng or "распак" in strng: continue
        r1 = strng.replace("gb", "")
        r2 = r1.replace("-", "")
        r3 = r2.replace("tb", "")
        r4 = r3.replace("rfb", "")
        r5 = r4.replace("2021", "")
        r6 = r5.replace("2023", "")
        r7 = r6.replace(")", "")
        r8 = r7.replace("(", "")
        z = r8.replace(".", "")
        text = z.split()
        new_text = ' '.join(text)
        if "s/m" in new_text or "m/l" in new_text or appleWtch in new_text or aw in new_text:
            applewatch = processing_apple_watches(provisioner, new_text)
            if applewatch != "" and applewatch is not None:
                lst.append(applewatch)
        elif airPds in new_text or aP in new_text:
            airpods = processing_airpods(provisioner, new_text)
            if airpods != "" and airpods is not None:
                lst.append(airpods)
        elif "wi" in new_text or "lte" in new_text or "ipad" in new_text:
            ipad = processing_ipads(provisioner, new_text)
            if ipad != "" and ipad is not None:
                lst.append(ipad)
        elif ip in new_text or new_text.startswith("11") or new_text.startswith("12") or new_text.startswith("13") or new_text.startswith("14") or new_text.startswith("se"):
            iphone = processing_iphones(provisioner, new_text)
            if iphone != "" and iphone is not None:
                lst.append(iphone)
        elif mcbook in new_text or "air 13" in new_text or "air pro 13" in new_text or "air 15" in new_text:
            macbook = processing_macbooks(provisioner, new_text)
            if macbook != "" and macbook is not None:
                lst.append(macbook)
    return lst


def processing_apple_watches(provisioner, new_text):
    apple_watch = ""
    r9 = new_text.replace("mm", "")
    st = r9
    if "se1" in new_text: return
    if "se 2" in new_text:
        r10 = r9.replace("se 2", "se2")
    elif "se " in new_text:
        r10 = r9.replace("se", "se2")
        st = r10.replace("2022", "")
    arr_for_check = st.split()
    check = len(arr_for_check)
    if check < 3: return
    line = ' '.join(arr_for_check)
    if "se2" in line:
        ind = line.index("se2") + 4
        stfrom = line[ind:]
        arr = stfrom.split()
        length = arr[0]
        color = arr[1]
        size = ""
        if length == str("40"):
            size = "s/m"
        elif length == str("44"):
            size = "m/l"
        sm = stfrom.replace("s/m", "")
        ml = sm.replace("m/l", "")
        a = ml.split()
        if len(a) == 3:
            price = a[2]
            apple_watch = (str(dict_columns.get(provisioner)) + "Умные часы Apple Watch SE 2 (2022) " + length + "mm " + color + " " + size + " " + price)
        elif len(a) == 4:
            qty = int(a[2])
            if qty < 5: return
            price = a[3]
            apple_watch = (str(dict_columns.get(provisioner)) + "Умные часы Apple Watch SE 2 (2022) " + length + "mm " + color + " " + size + " " + price)
    if "s8" in new_text or "8 " in new_text:
        ind = 0
        if "8" in new_text:
            ind = st.find("8") + 1
        elif "s8" in new_text:
            ind = st.index("s8") + 2
        stfrom = st[ind:]
        arr = stfrom.split()
        ln = len(arr)
        if ln < 3: return
        length = arr[0]
        color = arr[1]
        if color == "grey" or color == "black" or color == "gray":
            color = "midnight"
        size = arr[2]
        if size != "s/m" or size != "m/l":
            size = arr[2]
        sm = stfrom.replace("s/m", "")
        ml = sm.replace("m/l", "")
        a = ml.split()
        if len(a) == 3:
            price = a[2]
            apple_watch = (str(dict_columns.get(provisioner)) + "Умные часы Apple Watch Series 8 " + length + "mm " + color + " " + size + " " + price)
        elif len(a) == 4:
            qty = int(a[2])
            if qty < 5: return
            price = a[3]
            apple_watch = (str(dict_columns.get(provisioner)) + "Умные часы Apple Watch Series 8 " + length + "mm " + color + " " + size + " " + price)
    return apple_watch


def processing_airpods(provisioner, new_text):
    airpods = ""
    r = new_text.replace(airPds.lower(), "")
    c = r.replace(aP.lower(), "")
    arr = c.split()
    ln = len(arr)
    color = arr[0]
    if color == "grey":
        color = "black"
    elif color == "white":
        color = "silver"
    if ln == 2:
        price = arr[1]
        airpods = (str(dict_columns.get(provisioner)) + aP + " " + color + " " + price)
    elif ln == 3:
        qty = int(arr[1])
        if qty < 5: return
        price = arr[2]
        airpods = (str(dict_columns.get(provisioner)) + aP + " " + color + " " + price)
    return airpods


def processing_ipads(provisioner, new_text):
    ipad = ""
    connection = "wi-fi"
    yearrepl = new_text.replace("2022", "")
    replspace = yearrepl.replace("space", "")
    fllrepl = replspace
    if "wifi+lte" in new_text:
        connection = "wi-fi + cellular"
        frepl = replspace.replace("wifi+lte", "")
        fllrepl = frepl
    elif "wi" in new_text:
        frepl = replspace.replace("wi", "")
        srepl = frepl.replace("fi", "")
        trepl = srepl.replace("wifi", "")
        fllrepl = trepl
    elif "lte" in new_text:
        connection = "wi-fi + cellular"
        srepl = replspace.replace("lte", "")
        fllrepl = srepl
    if " 5 " in fllrepl:
        ind = fllrepl.index(" 5 ") + 2
        stfrom = fllrepl[ind:]
        arr = stfrom.split()
        memory = arr[0]
        color = arr[1]
        if color == "gray" or color == "grey" or color == "black" or color == "spgrey" or color == "spgray":
            color = "space grey"
        ln = len(arr)
        if ln == 3:
            price = arr[2]
            ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad Air 5 (2022) 10,9\" " + connection + " " + memory + "Gb " + color + " " + price)
        elif ln == 4:
            qty = int(arr[2])
            if qty < 5: return
            price = arr[3]
            ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad Air 5 (2022) 10,9\" " + connection + " " + arr[0] + "Gb " + color + " " + price)
    elif " 9 " in fllrepl:
        ind = fllrepl.index(" 9 ") + 2
        stfrom = fllrepl[ind:]
        arr = stfrom.split()
        ln = len(arr)
        if ln < 2: return
        memory = arr[0]
        color = arr[1]
        if color == "gray" or color == "grey" or color == "spgrey" or color == "spgray":
            color = "space grey"
        elif color == "white":
            color = "silver"
        ln = len(arr)
        if ln == 3:
            price = arr[2]
            ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10,2\" " + memory + "Gb " + connection + " 9-е поколение " + color + " " + price)
        elif ln == 4:
            qty = int(arr[2])
            if qty < 5: return
            price = arr[3]
            ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10,2\" " + memory + "Gb " + connection + " 9-е поколение " + color + " " + price)
    elif " 10 " in fllrepl:
        ind = fllrepl.index(" 10 ") + 3
        stfrom = fllrepl[ind:]
        arr = stfrom.split()
        ln = len(arr)
        if ln < 2: return
        memory = arr[0]
        color = arr[1]
        if color == "white":
            color = "silver"
        if ln == 3:
            price = arr[2]
            ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10 (2022) " + connection + " 10,9\" " + memory + "gb " + color + " " + price)
        elif ln == 4:
            qty = int(arr[2])
            if qty < 5: return
            price = arr[3]
            ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad 10 (2022) " + connection + " 10,9\" " + memory + "gb " + color + " " + price)
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
        if ln < 2: return
        memory = arr[0]
        color = arr[1]
        if color == "white":
            color = "silver"
        elif color == "black" or color == "gray" or color == "grey" or color == "spgrey" or color == "spgray":
            color = "space grey"
        size = "gb"
        if memory == str("1") or memory == str("2"):
            size = "tb"
        memory = arr[0] + size
        if " 11 " in fllrepl:
            if ln == 3:
                price = arr[2]
                ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 11 (2022) " + connection + " " + memory + " " + color + " " + price)
            elif ln == 4:
                qty = int(arr[2])
                if qty < 5: return
                price = arr[3]
                ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 11 (2022) " + connection + " " + memory + " " + color + " " + price)
        elif " 12 " in fllrepl or " 129 " in fllrepl:
            if ln == 3:
                price = arr[2]
                ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 12 12,9' (2022) " + memory + " " + connection + " " + color + " " + price)
            elif ln == 4:
                qty = int(arr[2])
                if qty < 5: return
                price = arr[3]
                ipad = (str(dict_columns.get(provisioner)) + "Планшет Apple iPad Pro 12 12,9' (2022) " + memory + " " + connection + " " + color + " " + price)
    return ipad


def processing_iphones(provisioner, new_text):
    iphone = ""
    f = new_text.replace("+", "plus ")
    s = f.replace("space", "")
    arr = s.split()
    ln = len(arr)
    size = "GB"
    if ln < 3: return
    if " act " in s: return
    if arr[2] == "max" or arr[2] == "мах":
        model = arr[0] + " " + arr[1] + " " + arr[2]
        memory = arr[3]
        color = arr[4]
        price = arr[5]
        if color == "spgrey":
            color = "black"
        elif color == "white":
            color = "silver"
        if memory == str("1") or memory == str("2"):
            size = "TB"
        if ln == 6:
            iphone = (str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price)
        elif ln == 7:
            qty = int(arr[5])
            if qty < 5: return
            price = arr[6]
            iphone = (str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price)
    elif arr[1] == "pro":
        model = arr[0] + " " + arr[1]
        memory = arr[2]
        color = arr[3]
        price = arr[4]
        if color == "spgrey":
            color = "black"
        elif color == "white":
            color = "silver"
        if memory == str("1") or memory == str("2"): size = "TB"
        if ln == 5:
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
        elif ln == 6:
            qty = int(arr[4])
            if qty < 5: return
            price = arr[5]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
    elif "se" in new_text:
        if "40" in new_text or "44" in new_text: return
        model = arr[0]
        memory = arr[1]
        if ln == 4:
            color = arr[2]
            price = arr[3]
            if color == "white":
                color = "starlight"
            elif color == "midnight":
                color = "black"
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
        elif ln == 5:
            qty = int(arr[4])
            if qty < 5: return
            if memory == str("3"):
                model = "se3"
                memory = arr[2]
            color = arr[3]
            if color == "white":
                color = "starlight"
            elif color == "midnight":
                color = "black"
            else: return
            price = arr[5]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
    elif arr[1] == "mini":
        model = arr[0] + " " + arr[1]
        memory = arr[2]
        color = arr[3]
        if color == "midnight":
            color = "black"
        elif color == "silver" or color == "starlight":
            color = "white"
        if ln == 5:
            price = arr[4]
            if memory == str("1") or memory == str("2"): size = "TB"
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
        elif ln > 5:
            qty = int(arr[4])
            if qty < 5: return
            price = arr[5]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
    elif arr[1].lower() == "plus":
        model = arr[0] + " " + arr[1]
        memory = arr[2]
        if memory == str("1") or memory == str("2"): size = "TB"
        color = arr[3].lower()
        if color == "white":
            color = "starlight"
        elif color == "black":
            color = "midnight"
        if ln == 5:
            price = arr[4]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
        else:
            qty = int(arr[4])
            if qty < 5: return
            price = arr[5]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
    elif arr[0].startswith("1"):
        model = arr[0]
        memory = arr[1]
        color = arr[2].lower()
        if model == "11":
            if color == "midnight":
                color = "black"
            elif color == "starlight" or color == "silver":
                color = "white"
        if model == "13" or model == "14":
            if color == "black":
                color = "midnight"
            elif color == "white" or color == "silver":
                color = "starlight"
        if memory == str("1") or memory == str("2"): size = "TB"
        if ln == 4:
            price = arr[3]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
        else:
            qty = int(arr[3])
            if qty < 5: return
            price = arr[4]
            iphone = str(dict_columns.get(provisioner)) + ip + " " + model + " " + memory + size + " " + color + " " + price
    return iphone


def processing_macbooks(provisioner, new_text):
    macbook = ""
    line = new_text.replace("/", " ")
    arr = line.split()
    model = ""
    price = ""
    for characteristic in arr:
        if characteristic.startswith("m"):
            if len(characteristic) == 5:
                model = characteristic
        if characteristic.isnumeric():
            if len(characteristic) == 5 or len(characteristic) == 6:
                price = characteristic
    if len(model) == 5 and len(price) == 5 or len(model) == 5 and len(price) == 6:
        macbook = (str(dict_columns.get(provisioner)) + model + " " + price)
    return macbook
