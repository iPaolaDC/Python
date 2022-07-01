import time


def time_to_go():
    # Verificamos la hora
    time_h = time.strftime('%H')
    time_m = time.strftime('%M')
    print("Esta es la hora", time_h, ":", time_m)

    # Validamos la hora de salida
    if int(time_h) >= 19:
        print("Es hora de ir a casa")
    else:
        time_left = 19 - int(time_h)
        print("Te quedan", time_left, "horas para salir")


if __name__ == '__main__':
    time_to_go()
