def lenguaje(linea_1):
    idioma = 0
    if "PT" in linea_1:
        idioma = "Portugués"
    if "ES" in linea_1:
        idioma = "Español"
    return idioma


def pais_cabina(pais):
    pais_de_cabina = 0
    # Cargamos el importe base en funcion de encuentra ubicada la cabina de peaje:
    if pais == "0":
        # Argentina
        pais_de_cabina = "Argentina"
    if pais == "1":
        # Bolivia
        pais_de_cabina = "Bolivia"
    if pais == "2":
        # Brasil
        pais_de_cabina = "Brasil"
    if pais == "3":
        # Paraguay
        pais_de_cabina = "Paraguay"
    if pais == "4":
        # Uruguay
        pais_de_cabina = "Uruguay"

    return pais_de_cabina


def ticket(tipo, telepeaje, pais_de_cabina):
    tarifa = 0
    if pais_de_cabina == "Argentina":
        tarifa = 300
    if pais_de_cabina == "Brasil":
        tarifa = 400
    if pais_de_cabina == "Uruguay":
        tarifa = 300
    if pais_de_cabina == "Paraguay":
        tarifa = 300
    if pais_de_cabina == "Bolivia":
        tarifa = 200
    # moto
    if tipo == "0":
        tarifa = int(tarifa*0.5)
        if telepeaje == "2":
            tarifa = int(tarifa*0.9)
    # auto
    if tipo == "1":
        tarifa = tarifa
        if telepeaje == "2":
            tarifa = int(tarifa*0.9)
    # camion
    if tipo == "2":
        tarifa = (tarifa*1.6)
        if telepeaje == "2":
            tarifa = int(tarifa-(tarifa*0.1))

    return tarifa


def porcentaje(carg, cbol, cbra, cchi, cpar, curu, cotr):
    cant_total_patentes = carg+cbol+cbra+cchi+cpar+curu+cotr
    porcentaje_otros = ((cotr*100)/cant_total_patentes)
    return porcentaje_otros


def promedio(cantidad, total):
    if cantidad > 0:
        return round(total / cantidad, 2)
    else:
        return 0


def test():
    file = open("peaje100.txt", "rt")
    linea = file.readline().upper()

    idioma = lenguaje(linea)
    # contador de patentes
    carg = cbol = cbra = cchi = cpar = curu = cotr = 0
    imp_acu_total = 0
    primera = 0
    cpp = 0
    bandera_patente = True
    mayimp = 0
    maypat = 0
    es_el_primero = True
    suma_kilometros = 0
    cant_vehiculos_arg_por_brasil = 0

    while True:
        linea = file.readline().upper()
        if linea == "":
            break

        # Recorremos cada linea
        patente = linea[0:7]
        tipo_vehiculo = linea[7:8]
        telepeaje = linea[8:9]
        pais = linea[9:10]
        kilometros = float(linea[10:13])
        tamanio_patente = len(patente)
        procedencia_vehiculo = 0

        # canculo de cantidad de patentes y pais de cada patente
        if tamanio_patente == 7:
            # filtramos patente por pais
            if patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
                # argentina
                procedencia_vehiculo = "Argentina"
                carg += 1
            elif patente[0:3].isalpha() and patente[3].isdigit() and patente[4].isalpha() and patente[5:7].isdigit():
                # brasil
                cbra += 1
            elif patente[0] == " " and patente[1:5].isalpha() and patente[5:7].isdigit():
                # chile
                cchi += 1
            elif patente[0:2].isalpha() and patente[2:].isdigit():
                # Bolivia
                cbol += 1
            elif patente[0:4].isalpha() and patente[4:].isdigit():
                # paraguay
                cpar += 1
            elif patente[0:3].isalpha() and patente[3:].isdigit():
                # uruguay
                curu += 1
            else:
                # otro
                cotr += 1
        else:
            # otro
            cotr += 1

        # Importe base
        importe_vehiculo = ticket(tipo_vehiculo, telepeaje, pais_cabina(pais))
        imp_acu_total += importe_vehiculo

        # Primera patente
        if bandera_patente:
            primera = patente
            bandera_patente = False
            cpp += 1
        elif primera == patente:
            cpp += 1

        # Mayor importe final cobrado
        if es_el_primero:
            mayimp = importe_vehiculo
            maypat = patente
            es_el_primero = False

        if importe_vehiculo > mayimp:
            mayimp = importe_vehiculo
            maypat = patente

        # Distancias recorridas
        if procedencia_vehiculo == "Argentina" and pais_cabina(pais) == "Brasil":
            cant_vehiculos_arg_por_brasil += 1
            suma_kilometros += kilometros
    # promedio de las distancias recorridas
    prom = promedio(cant_vehiculos_arg_por_brasil, suma_kilometros)

    # porcentaje otras patentes
    porc = porcentaje(carg, cbol, cbra, cchi, cpar, curu, cotr)

    print('(r1) - Idioma a usar en los informes:', idioma)

    print()
    print('(r2) - Cantidad de patentes de Argentina:', carg)
    print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    print('(r2) - Cantidad de patentes de Brasil:', cbra)
    print('(r2) - Cantidad de patentes de Chile:', cchi)
    print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    print('(r2) - Cantidad de patentes de Uruguay:', curu)
    print('(r2) - Cantidad de patentes de otro país:', cotr)
    print()
    print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)
    print()
    print('(r4) - Primera patente del archivo:', primera, '- Frecuencia deaparición: ', cpp)
    print()
    print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe: ', maypat)
    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
    print()
    print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas: ', prom, '\bkm')
    file.close()


test()
