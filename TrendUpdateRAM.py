import time
import rrdtool
from getSNMP import consultaSNMP
from trendGraphDetection import graphRAM
import _thread
from Parte3.Notify import send_alert_attached
carga = 0

def RAM(com,ip):
    bandera = 0
    t = 60
    while 1:
        carga = int(consultaSNMP(com,ip,'1.3.6.1.4.1.2021.4.6.0'))
        valor = "N:" + str(carga)
        print (valor)
        rrdtool.update('trendRAM.rrd', valor)
        rrdtool.dump('trendRAM.rrd','trendRAM.xml')
        graphRAM()
        if bandera == 0:
            if carga > 302342:
                _thread.start_new_thread(send_alert_attached, ("Sobrepasa 3 GB RAM Daniel Benitez Lopez", 'RAM'))
                bandera = 1
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)