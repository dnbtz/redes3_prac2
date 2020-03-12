import rrdtool


def create(nom):
    ret = rrdtool.create(nom+".rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:CPUload:GAUGE:600:U:U",
                         "RRA:AVERAGE:0.5:1:24")
    if ret:
        print(rrdtool.error())

def createRAM(nom):
    ret2 = rrdtool.create(nom+".rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:RAMload:GAUGE:600:U:U",
                         "RRA:AVERAGE:0.5:1:24")
    if ret2:
        print(rrdtool.error())


def createHDD(nom):
    ret2 = rrdtool.create(nom+".rrd",
                         "--start", 'N',
                         "--step", '60',
                         "DS:HDDload:GAUGE:600:U:U",
                         "RRA:AVERAGE:0.5:1:24")
    if ret2:
        print(rrdtool.error())
