from opcua import ua
from datetime import datetime
import time

from app.conexion import cliente_opc_create

client = cliente_opc_create()

variables_inversor = ["pa","pa_peak","ea","ea_hoy","estado","temperatura",
    "raislamiento","v1","v2","v3","i1","i2", "i3",
    "vs1","vs2","vs3","vs4","vs5","vs6","vs7","vs8","vs9","vs10",
    "is1","is2","is3","is4","is5","is6","is7","is8","is9","is10"]
variables_aarr = ["pa","pa1","pa2","pa3","ea","v1","v2","v3","i1","i2", "i3"]
variables_emi = ["rad1","rad2","tamb","tpanel"]

variables_pcs = ['pa_carga','pa_descarga','estado','pa','temperatura','raislamiento','ea','ea_hoy','regulacion','v1','v2','v3','i1','i2','i3']
variables_bomba = ['estado','pa','frecuencia','horas']
variables_bat = ['bcu1_estado','bcu1_v','bcu1_i', 'bcu1_pa', 'bcu1_soc', 'bcu1_soh', 'bcu1_soe', 'bcu1_dod', 'bcu1_capacidad_carga', 'bcu1_capacidad_descarga',
    'bcu2_estado', 'bcu2_v', 'bcu2_i', 'bcu2_pa', 'bcu2_soc', 'bcu2_soh', 'bcu2_soe', 'bcu2_dod', 'bcu2_capacidad_carga', 'bcu2_capacidad_descarga',
    'temp_cabin1', 'temp_cabin2', 'temp_cabin3', 'temp_cabin4', 'estado_cont1','estado_cont2','estado_cont3',
    'soc','pa','ea_carga','ea_descarga','ea_carga_hoy','ea_descarga_hoy','capacidad_carga','capacidad_descarga',
    'v1', 'v2','v3' ,'i1', 'i2', 'i3' ]

def MarcaTemporal():
    presentDate = datetime.now()
    unix_timestamp = datetime.timestamp(presentDate)*1000
    return(unix_timestamp)

def obtenerNodos():
    root = client.get_root_node()
    children = root.get_children()
    child_of_children=children[0].get_children()
    variables = {}
    for x in range(2, len(child_of_children)):
        c_child_of_children=child_of_children[x].get_children()
        for i in range(len(c_child_of_children)):
            variables.update({i : str(client.get_node(c_child_of_children[i]))})
    return(variables)

def leerNodo(variable):
    value = client.get_node(variable)
    value = value.get_value()
    return(value)

def escribirNodo(valor, variable):
    node = client.get_node(variable)
    value1 = node.get_value()
    try:
        node.set_value(ua.DataValue(ua.Variant(valor, ua.VariantType.Double)))
    except:
        node.set_value(ua.DataValue(ua.Variant(valor, ua.VariantType.Int64)))
    value2 = node.get_value()
    return(value1, value2)

def ObtenerInversor(num_equipo):
    definicion = "ns=2;s=Inversor" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_inversor]
    data = {"fecha": MarcaTemporal(), "inversor": num_equipo}
    for i in range(len(variables)):
        data.update({variables_inversor[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerAARR(num_equipo):
    definicion = "ns=2;s=AARR" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_aarr]
    data = {"fecha": MarcaTemporal(), "aarr": num_equipo}
    for i in range(len(variables)):
        data.update({variables_aarr[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerEMI(num_equipo):
    definicion = "ns=2;s=EMI" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_emi]
    data = {"fecha": MarcaTemporal(), "emi": num_equipo}
    for i in range(len(variables)):
        data.update({variables_emi[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerPCS(num_equipo):
    definicion = "ns=2;s=PCS" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_pcs]
    data = {"fecha": MarcaTemporal(), "pcs": num_equipo}
    for i in range(len(variables)):
        data.update({variables_pcs[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerBateria(num_equipo):
    definicion = "ns=2;s=Bateria" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_bat]
    data = {"fecha": MarcaTemporal(), "bateria": num_equipo}
    for i in range(len(variables)):
        data.update({variables_bat[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerBomba(num_equipo):
    definicion = "ns=2;s=Bomba" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_bomba]
    data = {"fecha": MarcaTemporal(), "bomba": num_equipo}
    for i in range(len(variables)):
        data.update({variables_bomba[i]:client.get_node((variables[i])).get_value()})
    return(data)

def escribirInversor(data):
    data = data.__dict__
    num_equipo = data['inversor']
    del data['inversor']
    definicion = "ns=2;s=Inversor" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_inversor]
    variables_nomodificadas = []
    for i in range(len(data)):
        #print({variables[i]:data[variables_inversor[i]]})
        try:
            client.get_node(variables[i]).set_value(ua.DataValue(ua.Variant(data[variables_inversor[i]], ua.VariantType.Double)))
        except:
            variables_nomodificadas.append(variables[i])
    return(variables_nomodificadas)

def escribirAARR(data):
    data = data.__dict__
    num_equipo = data['aarr']
    del data['aarr']
    definicion = "ns=2;s=AARR" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_aarr]
    variables_nomodificadas = []
    for i in range(len(data)):
        try:
            client.get_node(variables[i]).set_value(ua.DataValue(ua.Variant(data[variables_aarr[i]], ua.VariantType.Double)))
        except:
            variables_nomodificadas.append(variables[i])
    return(variables_nomodificadas)

def escribirEMI(data):
    data = data.__dict__
    num_equipo = data['emi']
    del data['emi']
    definicion = "ns=2;s=EMI" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_emi]
    variables_nomodificadas = []
    for i in range(len(data)):
        try:
            client.get_node(variables[i]).set_value(ua.DataValue(ua.Variant(data[variables_emi[i]], ua.VariantType.Double)))
        except:
            variables_nomodificadas.append(variables[i])
    return(variables_nomodificadas)

def escribirPCS(data):
    data = data.__dict__
    num_equipo = data['pcs']
    del data['pcs']
    definicion = "ns=2;s=PCS" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_pcs]
    variables_nomodificadas = []
    for i in range(len(data)):
        try:
            client.get_node(variables[i]).set_value(ua.DataValue(ua.Variant(data[variables_pcs[i]], ua.VariantType.Double)))
        except:
            variables_nomodificadas.append(variables[i])
    return(variables_nomodificadas)

def escribirBateria(data):
    data = data.__dict__
    num_equipo = data['bateria']
    del data['bateria']
    definicion = "ns=2;s=Bateria" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_bat]
    variables_nomodificadas = []
    for i in range(len(data)):
        try:
            client.get_node(variables[i]).set_value(ua.DataValue(ua.Variant(data[variables_bat[i]], ua.VariantType.Double)))
        except:
            variables_nomodificadas.append(variables[i])
    return(variables_nomodificadas)

def escribirBomba(data):
    data = data.__dict__
    num_equipo = data['bomba']
    del data['bomba']
    definicion = "ns=2;s=Bomba" + str(num_equipo) + "."
    variables = [definicion + s for s in variables_bomba]
    variables_nomodificadas = []
    for i in range(len(data)):
        try:
            client.get_node(variables[i]).set_value(ua.DataValue(ua.Variant(data[variables_bomba[i]], ua.VariantType.Double)))
        except:
            variables_nomodificadas.append(variables[i])
    return(variables_nomodificadas)