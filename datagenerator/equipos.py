
async def activar_writable(valores):
    for valor in valores:
        await valor.set_writable()

async def InversorSchema(server, idx, nombre_inversor):    
    myobj = await server.nodes.objects.add_object(idx, nombre_inversor)

    #Valores Inversor
    PA = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".pa", "pa", 10.5)
    PA_peak = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".pa_peak", "Ppa_peak", 10.5)
    EA = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".ea", "ea", 26.7)
    EA_hoy = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".ea_hoy", "ea_hoy", 0.0)
    Estado = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".estado", "estado", 12)
    Temperatura = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".temperatura", "temperatura", 58)
    Raislamiento = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".raislamiento", "raislamiento", 950)

    # Valores Alterna
    V1 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".v1", "v1", 0.0)
    V2 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".v2", "v2", 0.0)
    V3 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".v3", "v3", 0.0)
    I1 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".i1", "i1", 0.0)
    I2 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".i2", "i2", 0.0)
    I3 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".i3", "i3", 0.0)

    #Tensiones Strings
    vs1 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs1", "vs1", 0.0)
    vs2 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs2", "vs2", 0.0)
    vs3 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs3", "vs3", 0.0)
    vs4 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs4", "vs4", 0.0)
    vs5 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs5", "vs5", 0.0)
    vs6 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs6", "vs6", 0.0)
    vs7 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs7", "vs7", 0.0)
    vs8 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs8", "vs8", 0.0)
    vs9 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs9", "vs9", 0.0)
    vs10 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".vs10", "vs10", 0.0)

    # Intensidad Strings
    is1 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is1", "is1", 0.0)
    is2 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is2", "is2", 0.0)
    is3 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is3", "is3", 0.0)
    is4 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is4", "is4", 0.0)
    is5 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is5", "is5", 0.0)
    is6 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is6", "is6", 0.0)
    is7 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is7", "is7", 0.0)
    is8 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is8", "is8", 0.0)
    is9 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is9", "is9", 0.0)
    is10 = await myobj.add_variable("ns=2;s=" + nombre_inversor + ".is10", "is10", 0.0)

    v_string = [ vs1, vs2, vs3, vs4, vs5, vs6, vs7, vs8, vs9, vs10 ]
    i_string = [ is1, is2, is3, is4, is5, is6, is7, is8, is9, is10 ]
    parametros_inv = [ PA, PA_peak, EA, EA_hoy, Estado, V1, V2, V3, I1, I2, I3, Temperatura, Raislamiento]

    await activar_writable(parametros_inv)
    return(v_string, i_string)

async def AARRSchema(server, idx, nombre_aarr):    
    myobj = await server.nodes.objects.add_object(idx, nombre_aarr)

    V1 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".v1", "v1", 0.0)
    V2 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".v2", "v2", 0.0)
    V3 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".v3", "v3", 0.0)
    I1 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".i1", "i1", 0.0)
    I2 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".i2", "i2", 0.0)
    I3 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".i3", "i3", 0.0)
    PA1 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".pa1", "pa1", 0.0)
    PA2 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".pa2", "pa2", 0.0)
    PA3 = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".pa3", "pa3", 0.0)
    PA = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".pa", "Ppa", 0.0)
    EA = await myobj.add_variable("ns=2;s=" + nombre_aarr + ".ea", "ea", 0.0)

    parametros_aarr = [ PA, PA1, PA2, PA3, EA ]
    tensiones_aarr = [ V1, V2, V3 ]
    intensidades_aarr = [ I1, I2, I3 ]

    await activar_writable(parametros_aarr)
    return(tensiones_aarr, intensidades_aarr)

async def EMISchema(server, idx, nombre_emi):    
    myobj = await server.nodes.objects.add_object(idx, nombre_emi)

    # Radiaciones
    Rad1 = await myobj.add_variable("ns=2;s=" + nombre_emi + ".rad1", "rad1", 0.0)
    Rad2 = await myobj.add_variable("ns=2;s=" + nombre_emi + ".rad2", "rad2", 0.0)

    #Temperaturas
    Tamb = await myobj.add_variable("ns=2;s=" + nombre_emi + ".tamb", "tamb", 0.0)
    Tpanel = await myobj.add_variable("ns=2;s=" + nombre_emi + ".tpanel", "tpanel", 0.0)

    radiaciones_emi = [ Rad1, Rad2 ]
    temperaturas_emi = [ Tamb, Tpanel ]
    return(radiaciones_emi, temperaturas_emi)