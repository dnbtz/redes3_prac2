import sys
import math
import rrdtool
import time
from Parte3.Notify import send_alert_attached
#rrdpath = '/home/Daniel/Documents/RedesTres/P2OK/AdministracionServiciosRred/Practica2/'

def graphCPU():
    ultima_lectura = int(rrdtool.last("trendCPU.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 600

    ret = rrdtool.graphv( "deteccionCPU.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=Cpu load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                         "DEF:cargaCPU=trendCPU.rrd:CPUload:AVERAGE",

                         "CDEF:umbral30=cargaCPU,30,LT,0,cargaCPU,IF",
                         "CDEF:umbral60=cargaCPU,60,LT,0,cargaCPU,IF",
                         "CDEF:umbral80=cargaCPU,80,LT,0,cargaCPU,IF",
                         "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                         "VDEF:cargaMIN=cargaCPU,MINIMUM",
                         "VDEF:cargaSTDEV=cargaCPU,STDEV",
                         "VDEF:cargaLAST=cargaCPU,LAST",
                         "AREA:cargaCPU#00FF00:Carga del CPU",
                         "AREA:umbral30#FF9F00:Carga CPU mayor que 30",
                         "AREA:umbral60#FF9F70:Carga CPU mayor que 60",
                         "AREA:umbral80#FF0000:Carga CPU mayor que 80",
                         "HRULE:30#00FF00:Umbral 1 - 30%",
                         "HRULE:60#FF9F00:Umbral 31 - 60%",
                         "HRULE:80#FF9F70:Umbral 61 - 80%",
                         "HRULE:100#FF0000:Umbral 81 - 100%",
                         "PRINT:cargaLAST:%6.2lf %SLAst",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )


def graphRAM():
    ultima_lectura = int(rrdtool.last("trendRAM.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 600

    ret = rrdtool.graphv( "deteccionRAM.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=RAM load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                         "DEF:cargaRAM=trendRAM.rrd:RAMload:AVERAGE",

                         "CDEF:umbral25=cargaRAM,250000,LT,0,cargaRAM,IF",
                         "CDEF:umbral30=cargaRAM,300000,LT,0,cargaRAM,IF",
                         "CDEF:umbral35=cargaRAM,350000,LT,0,cargaRAM,IF",
                         "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                         "VDEF:cargaMIN=cargaRAM,MINIMUM",
                         "VDEF:cargaSTDEV=cargaRAM,STDEV",
                         "VDEF:cargaLAST=cargaRAM,LAST",
                         "AREA:cargaRAM#00FF00:Carga de la RAM",
                         "AREA:umbral25#FF9F00:Carga RAM mayor que 2.5GB",
                         "AREA:umbral30#FF9F70:Carga RAM mayor que 3GB",
                         "AREA:umbral35#FF0000:Carga RAM mayor que 3.5GB",
                         "HRULE:200000#00FF00:Umbral 2GB",
                         "HRULE:250000#FF9F00:Umbral 2.5GB",
                         "HRULE:300000#FF9F70:Umbral 3GB",
                         "HRULE:350000#FF0000:Umbral 3.5GB",
                         "PRINT:cargaLAST:%6.2lf %SLAst",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )


def graphHDD():
    ultima_lectura = int(rrdtool.last("trendHDD.rrd"))
    tiempo_final = ultima_lectura
    tiempo_inicial = tiempo_final - 600

    ret = rrdtool.graphv( "deteccionHDD.png",
                         "--start",str(tiempo_inicial),
                         "--end",str(tiempo_final),
                         "--vertical-label=HDD load",
                        '--lower-limit', '0',
                        '--upper-limit', '100',
                         "DEF:cargaHDD=trendHDD.rrd:HDDload:AVERAGE",

                         "CDEF:umbral30=cargaHDD,30,LT,0,cargaHDD,IF",
                         "CDEF:umbral60=cargaHDD,60,LT,0,cargaHDD,IF",
                         "CDEF:umbral80=cargaHDD,80,LT,0,cargaHDD,IF",
                         "VDEF:cargaMAX=cargaHDD,MAXIMUM",
                         "VDEF:cargaMIN=cargaHDD,MINIMUM",
                         "VDEF:cargaSTDEV=cargaHDD,STDEV",
                         "VDEF:cargaLAST=cargaHDD,LAST",
                         "AREA:cargaHDD#00FF00:Carga del HDD",
                         "AREA:umbral30#FF9F00:Carga HDD mayor que 30",
                         "AREA:umbral60#FF9F70:Carga HDD mayor que 60",
                         "AREA:umbral80#FF0000:Carga HDD mayor que 80",
                         "HRULE:30#00FF00:Umbral 1 - 30%",
                         "HRULE:60#FF9F00:Umbral 31 - 60%",
                         "HRULE:80#FF9F70:Umbral 61 - 80%",
                         "HRULE:100#FF0000:Umbral 81 - 100%",
                         "PRINT:cargaLAST:%6.2lf %SLAst",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST" )
