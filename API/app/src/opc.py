from opcua import ua
from app.conexion import cliente_opc_create

client = cliente_opc_create()

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
    variables = ["PA","PA_peak","EA","EA_hoy","Estado","Temperatura",
        "Raislamiento","V1","V2","V3","I1","I2", "I3",
        "vs1","vs2","vs3","vs4","vs5","vs6","vs7","vs8","vs9","vs10",
        "is1","is2","is3","is4","is5","is6","is7","is8","is9","is10"]
    definicion = "ns=2;s=Inversor" + str(num_equipo) + "."
    variables = [definicion + s for s in variables]
    data = {}
    for i in range(len(variables)):
        data.update({variables[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerAARR(num_equipo):
    variables = ["PA","PA1","PA2","PA3","EA",
        "V1","V2","V3","I1","I2", "I3"]
    definicion = "ns=2;s=AARR" + str(num_equipo) + "."
    variables = [definicion + s for s in variables]
    data = {}
    for i in range(len(variables)):
        data.update({variables[i]:client.get_node((variables[i])).get_value()})
    return(data)

def ObtenerEMI(num_equipo):
    variables = ["Rad1","Rad2","Tamb","Tpanel"]
    definicion = "ns=2;s=EMI" + str(num_equipo) + "."
    variables = [definicion + s for s in variables]
    data = {}
    for i in range(len(variables)):
        data.update({variables[i]:client.get_node((variables[i])).get_value()})
    return(data)