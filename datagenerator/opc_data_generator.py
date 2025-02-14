import asyncio
import logging
import random
from asyncua import Server, ua

from equipos import InversorSchema, AARRSchema, EMISchema, PCSSchema, BateriaSchema, VariadorSchema, DiferencialSchema

vs_min_val = 500
vs_max_val = 700

is_min_val = 7
is_max_val = 12

temp_min_val = 10
temp_max_val = 35

rad_min_val = 360
rad_max_val = 1200

tensiones_min_val = 380
tensiones_max_val = 410

intensidades_min_val = 10
intensidades_max_val = 45

async def main():
    #_logger = logging.getLogger("asyncua")
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/pavener/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    (v_string_Inv1, i_string_Inv1) = await InversorSchema(server, idx, "Inversor1")
    (tensiones_aarr, intensidades_aarr) = await AARRSchema(server, idx, "AARR1")
    (radiaciones_emi1, temperaturas_emi1) = await EMISchema(server, idx, "EMI1")
    (tensiones_pcs, intensidades_pcs) = await PCSSchema(server, idx, "PCS1")
    (tensiones_bateria, intensidades_bateria) = await BateriaSchema(server, idx, "Bateria1")
    await VariadorSchema(server, idx, "Bomba1")
    await DiferencialSchema(server, idx, "Diferencial1")
  
    #_logger.info("Starting server!")
    async with server:
        while True:
            await asyncio.sleep(1)
            for opc in v_string_Inv1:
                new_val = round(random.uniform(vs_min_val, vs_max_val),2)
                #_logger.info("Set value of %s to %.1f", opc, new_val)
                await opc.write_value(new_val)
            for opc in i_string_Inv1:
                new_val = round(random.uniform(is_min_val, is_max_val),2)
                await opc.write_value(new_val)
            for opc in tensiones_aarr:
                new_val = round(random.uniform(tensiones_min_val, tensiones_max_val),2)
                await opc.write_value(new_val)
            for opc in intensidades_aarr:
                new_val = round(random.uniform(intensidades_min_val, intensidades_max_val),2)
                await opc.write_value(new_val)
            for opc in radiaciones_emi1:
                new_val = round(random.uniform(rad_min_val, rad_max_val),2)
                await opc.write_value(new_val)
            for opc in temperaturas_emi1:
                new_val = round(random.uniform(temp_min_val, temp_max_val),2)
                await opc.write_value(new_val)
            
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)