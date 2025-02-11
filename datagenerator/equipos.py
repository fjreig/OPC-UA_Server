
async def activar_writable(valores):
    for valor in valores:
        await valor.set_writable()

async def InversorSchema(server, idx, nombre_inversor):
    ns = "ns=2;s=" + nombre_inversor + ".PA"
    ns1 = "ns=2;s=" + nombre_inversor + ".EA"
    ns2 = "ns=2;s=" + nombre_inversor + ".EA_hoy"

    ns3 = "ns=2;s=" + nombre_inversor + ".vs1"
    ns4 = "ns=2;s=" + nombre_inversor + ".vs2"
    ns5 = "ns=2;s=" + nombre_inversor + ".vs3"
    ns6 = "ns=2;s=" + nombre_inversor + ".vs4"
    ns7 = "ns=2;s=" + nombre_inversor + ".vs5"
    ns8 = "ns=2;s=" + nombre_inversor + ".vs6"
    ns9 = "ns=2;s=" + nombre_inversor + ".vs7"
    ns10 = "ns=2;s=" + nombre_inversor + ".vs8"
    ns11 = "ns=2;s=" + nombre_inversor + ".vs9"
    ns12 = "ns=2;s=" + nombre_inversor + ".vs10"

    ns13 = "ns=2;s=" + nombre_inversor + ".is1"
    ns14 = "ns=2;s=" + nombre_inversor + ".is2"
    ns15 = "ns=2;s=" + nombre_inversor + ".is3"
    ns16 = "ns=2;s=" + nombre_inversor + ".is4"
    ns17 = "ns=2;s=" + nombre_inversor + ".is5"
    ns18 = "ns=2;s=" + nombre_inversor + ".is6"
    ns19 = "ns=2;s=" + nombre_inversor + ".is7"
    ns20 = "ns=2;s=" + nombre_inversor + ".is8"
    ns21 = "ns=2;s=" + nombre_inversor + ".is9"
    ns22 = "ns=2;s=" + nombre_inversor + ".is10"
    
    myobj = await server.nodes.objects.add_object(idx, nombre_inversor)
    PA = await myobj.add_variable(ns, "PA", 10.5)
    EA = await myobj.add_variable(ns1, "EA", 26.7)
    EA_hoy = await myobj.add_variable(ns2, "EA_hoy", 0.0)

    vs1 = await myobj.add_variable(ns3, "vs1", 0.0)
    vs2 = await myobj.add_variable(ns4, "vs2", 0.0)
    vs3 = await myobj.add_variable(ns5, "vs3", 0.0)
    vs4 = await myobj.add_variable(ns6, "vs4", 0.0)
    vs5 = await myobj.add_variable(ns7, "vs5", 0.0)
    vs6 = await myobj.add_variable(ns8, "vs6", 0.0)
    vs7 = await myobj.add_variable(ns9, "vs7", 0.0)
    vs8 = await myobj.add_variable(ns10, "vs8", 0.0)
    vs9 = await myobj.add_variable(ns11, "vs9", 0.0)
    vs10 = await myobj.add_variable(ns12, "vs10", 0.0)

    is1 = await myobj.add_variable(ns13, "is1", 0.0)
    is2 = await myobj.add_variable(ns14, "is2", 0.0)
    is3 = await myobj.add_variable(ns15, "is3", 0.0)
    is4 = await myobj.add_variable(ns16, "is4", 0.0)
    is5 = await myobj.add_variable(ns17, "is5", 0.0)
    is6 = await myobj.add_variable(ns18, "is6", 0.0)
    is7 = await myobj.add_variable(ns19, "is7", 0.0)
    is8 = await myobj.add_variable(ns20, "is8", 0.0)
    is9 = await myobj.add_variable(ns21, "is9", 0.0)
    is10 = await myobj.add_variable(ns22, "is10", 0.0)

    v_string = [ vs1, vs2, vs3, vs4, vs5, vs6, vs7, vs8, vs9, vs10 ]
    i_string = [ is1, is2, is3, is4, is5, is6, is7, is8, is9, is10 ]
    parametros_inv = [ PA, EA, EA_hoy]

    await activar_writable(parametros_inv)

    return(v_string, i_string)