from airPods import airPods
from iPhone import iPhone



ip = "iphone"
airPds = "Air Pods"
aP = "AirPods"
iPd = "iPad"
appleWtch = "Apple Watch"
aw = "aw"
watch = "Watch"
mcbook = "Macbook"


def get_decoding_report(file):
    report = open(file)
    lst = list()
    for i in report:
        i_encode = i.encode("ascii", "ignore")
        i_decode = i_encode.decode()
        if i_decode != "\n":
            lst.append(i_decode)
    return lst


def get_goods_list_from_price(file):
    l = get_decoding_report(file)
    mp = dict()
    for i in l:
        if ip in i or i.startswith("11") or i.startswith("12") or i.startswith("13") or i.startswith("14") or i.startswith("SE"):
            mp[i] = iPhone, l.index(i)
        elif airPds in i or aP in i:
            mp[i] = airPds, l.index(i)
        elif iPd in i:
            mp[i] = iPd, l.index(i)
        elif appleWtch in i or aw in i or watch in i:
            mp[i] = appleWtch, l.index(i)
        elif mcbook in i:
            mp[i] = mcbook, l.index(i)
    return mp


def get_goods_list_from_prices(file):
    provisioner = "братья"
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
        if ip in i or i.startswith("11") or i.startswith("12") or i.startswith("13") or i.startswith("14") or i.lower().startswith("se"):
            s = z.split()
            ln = len(s)
            size = "GB"
            if ln < 3: continue
            if s[2].lower() == "max":
                if s[3] == 1 or s[3] == 2:
                    size = "TB"
                if ln == 6:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1] + " " + s[2], s[3] + size, s[4], provisioner, s[5]))
                else:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1] + " " + s[2], s[3] + size, s[4], provisioner, s[6]))
            elif s[1].lower() == "pro":
                if s[2] == 1 or s[2] == 2: size = "TB"
                if ln == 5:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[4]))
                else:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[5]))
            elif "se" in i.lower():
                if s[1] == 1 or s[1] == 2: size = "TB"
                if ln == 4:
                    lst.append(iPhone(ip + " " + s[0], s[1] + size, s[2], provisioner, s[3]))
                else:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[5]))
            elif s[1].lower() == "mini":
                if ln == 5:
                    if s[2] == 1 or s[2] == 2: size = "TB"
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[4]))
                else:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[5]))
            elif s[1].lower() == "plus":
                if s[2] == 1 or s[2] == 2: size = "TB"
                if ln == 5:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[4]))
                else:
                    lst.append(iPhone(ip + " " + s[0] + " " + s[1], s[2] + size, s[3], provisioner, s[5]))
            elif s[0].startswith("1"):
                if ln == 4:
                    if s[1] == 1 or s[1] == 2: size = "TB"
                    lst.append(iPhone(ip + " " + s[0], s[1] + size, s[2].capitalize(), provisioner, s[3]))
                else:
                    lst.append(iPhone(ip + " " + s[0], s[1] + size, s[2].capitalize(), provisioner, s[4]))
        elif airPds in i or aP in i:
            r = i.split()
            if r[2].lower() == "pro":
                lst.append(airPods(airPds + " " + r[2] + " " + r[3] + " " + r[4], "", provisioner, r[6]))
            elif r[2].lower() == "max":
                lst.append(airPods(airPds + " " + r[2], r[3], provisioner, r[5]))
            else:
                lst.append(airPods(airPds + " " + r[2], "", provisioner, r[4]))
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
