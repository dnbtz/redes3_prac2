import time
import rrdtool
from getSNMP import consultaSNMP
from trendGraphDetection import graphHDD
import _thread
from Parte3.Notify import send_alert_attached
carga = 0

def HDD(com,ip):
    bandera = 0
    t = 60
    while 1:
        cargausado = int(consultaSNMP(com,ip,'1.3.6.1.2.1.25.2.3.1.6.36'))
        cargatotal = int(consultaSNMP(com, ip, '1.3.6.1.2.1.25.2.3.1.5.36'))
        carga = cargausado * 100 / cargatotal
        valor = "N:" + str(carga)
        print (valor)
        rrdtool.update('trendHDD.rrd', valor)
        rrdtool.dump('trendHDD.rrd','trendHDD.xml')
        graphHDD()
        if bandera == 0:
            if carga > 60:
                _thread.start_new_thread(send_alert_attached, ("Sobrepasa 60% Disco Daniel Benitez Lopez", 'HDD'))
                bandera = 1
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)