import asyncio
import logging
import random
from asyncua import Server, ua

from equipos import InversorSchema

vs_min_val = 500
vs_max_val = 700

is_min_val = 7
is_max_val = 12

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
                #_logger.info("Set value of %s to %.1f", opc, new_val)
                await opc.write_value(new_val)
            
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)