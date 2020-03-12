import time
import rrdtool
from getSNMP import consultaSNMP
from trendGraphDetection import graphCPU
import _thread
from Parte3.Notify import send_alert_attached
#OID de ram: 1.3.6.1.4.1.2021.4.6.0
carga = 0

def CPU(com,ip):
    bandera1 = 0
    bandera2 = 0
    bandera3 = 0
    t = 60
    while 1:
        carga = int(consultaSNMP(com,ip,'1.3.6.1.2.1.25.2.3.1.6.2'))
        valor = "N:" + str(carga)
        print (valor)
        rrdtool.update('trendCPU.rrd', valor)
        rrdtool.dump('trendCPU.rrd','trendCPU.xml')
        graphCPU()
        if bandera1 == 0:
            if carga > 30:
                _thread.start_new_thread(send_alert_attached, ("Sobrepasa 30% CPU Daniel Benitez Lopez", 'CPU'))
                #send_alert_attached("Sobrepasa Umbral línea base CPU", 'CPU')
                bandera1 = 1
        if bandera2 == 0:
            if carga > 60:
                _thread.start_new_thread(send_alert_attached, ("Sobrepasa 60% CPU Daniel Benitez Lopez", 'CPU'))
                #send_alert_attached("Sobrepasa Umbral línea base CPU", 'CPU')
                bandera2 = 1
        if bandera3 == 0:
            if carga > 80:
                _thread.start_new_thread(send_alert_attached, ("Sobrepasa 80% CPU Daniel Benitez Lopez", 'CPU'))
                #send_alert_attached("Sobrepasa Umbral línea base CPU", 'CPU')
                bandera3 = 1
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)