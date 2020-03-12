import threading
from trendCreate import create
from trendCreate import createRAM
from trendCreate import createHDD
from TrendUpdate import CPU
from TrendUpdateRAM import RAM
from TrendUpdateHDD import HDD

def main():
    print("Menu principal")
    print("1. Agregar agente")
    x = input("Opción: ")

    if x == '1':
        agrega()


def agrega():
    com = input("Dame la comunidad: ")
    ip = input("Dame la ip: ")
    create("trendCPU")
    #createRAM("trendRAM")
    #createHDD("trendHDD")
    x = threading.Thread(target=CPU, args=(com, ip))
    x.start()
    #y = threading.Thread(target=RAM, args=(com, ip))
    #y.start()
    #z = threading.Thread(target=HDD, args=(com, ip))
    #z.start()
    #CPU(com,ip)
    #RAM(com,ip)


main()