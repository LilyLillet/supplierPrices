ip = "iphone"
airPds = "Air Pods"
aP = "AirPods"
iPd = "iPad"
appleWtch = "Apple Watch"
aw = "aw"
watch = "Watch"
mcbook = "Macbook"

dict_columns = {
    'acer': "АСЕР",
    'brothers': "братья",
    'nikita': "никита",
    'tony': "тони",
    '112': "112",
}


def get_decoding_report(file):
    report = open(file)
    lst = list()
    for i in report:
        i_encode = i.encode("ascii", "ignore")
        i_decode = i_encode.decode()
        if i_decode != "\n":
            lst.append(i_decode)
    return lst


def get_goods_list_from_prices(file, filename):
    provisioner = filename
    l = get_decoding_report(file)
    lst = list()
    for i in l:
        n = i.lower().replace("gb", "")
        f = n.replace("-", "")
        o = f.replace("(2sim)", "")
        m = o.replace("2 sim", "")
        p = m.replace("2sim", "")
        x = p.replace("tb", "")
        y = x.replace("rfb", "")
        z = y.replace(".", "")
        if ip in i or i.startswith("11") or i.startswith("12") or i.startswith("13") or i.startswith(
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
                        str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + s[2] + " " + str(
                            s[3]) + size + " " + color + " " + str(s[5]))
                else:
                    lst.append(
                        str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + s[2] + " " + str(
                            s[3]) + size + " " + color + " " + str(s[6]))
            elif s[1].lower() == "pro":
                color = s[3]
                if color == "spgrey":
                    color = "black"
                elif color == "white":
                    color = "silver"
                if s[2] == str("1") or s[2] == str("2"): size = "TB"
                if ln == 5:
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[4]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif "se" in i.lower():
                if ln == 4:
                    color = s[2]
                    if color == "white":
                        color = "starlight"
                    elif color == "midnight":
                        color = "black"
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + str(
                        s[1]) + size + " " + color + " " + str(s[3]))
                else:
                    color = s[3]
                    if color == "white":
                        color = "starlight"
                    elif color == "midnight":
                        color = "black"
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + str(s[1]) + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif s[1].lower() == "mini":
                color = s[3]
                if color == "midnight":
                    color = "black"
                elif color == "silver" or color == "starlight":
                    color = "white"
                if ln == 5:
                    if s[2] == 1 or s[2] == 2: size = "TB"
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[4]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif s[1].lower() == "plus":
                if s[2] == 1 or s[2] == 2: size = "TB"
                color = s[3]
                if color == "white":
                    color = "starlight"
                elif color == "black":
                    color = "midnight"
                if ln == 5:
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[4]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + s[1] + " " + str(
                        s[2]) + size + " " + color + " " + str(s[5]))
            elif s[0].startswith("1"):
                color = s[2]
                if s[0] == "13" or s[0] == "14":
                    if color == "black":
                        color = "midnight"
                    elif color == "white" or color == "silver":
                        color = "starlight"
                if ln == 4:
                    if s[1] == 1 or s[1] == 2: size = "TB"
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + str(
                        s[1]) + size + " " + color + " " + str(s[3]))
                else:
                    lst.append(str(dict_columns.get(provisioner)) + " " + ip + " " + s[0] + " " + str(
                        s[1]) + size + " " + color + " " + str(s[4]))
        elif airPds in i or aP in i:
            r = i.split()
            if r[2].lower() == "pro":
                lst.append((airPds + " " + r[2] + " " + r[3] + " " + r[4], "", r[6]))
            elif r[2].lower() == "max":
                lst.append((airPds + " " + r[2], r[3], r[5]))
            else:
                lst.append((airPds + " " + r[2], "", r[4]))
        #            mp[i] = airPds, l.index(i)
        elif iPd in i:
            print("ipad")
        #           mp[i] = iPd, l.index(i)
        elif appleWtch in i or aw in i or watch in i:
            print("watch")
        #            mp[i] = appleWtch, l.index(i)
        elif mcbook in i:
            print("mac")
    #            mp[i] = mcbook, l.index(i)
    return lst
