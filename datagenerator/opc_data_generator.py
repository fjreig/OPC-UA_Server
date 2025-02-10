import asyncio
import logging
import random
from asyncua import Server, ua

async def main():
    _logger = logging.getLogger("asyncua")
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)
    ns = "ns=2;s=Inversor1.PA"
    ns2 = "ns=2;s=Inversor1.EA"
    ns4 = "ns=2;s=Inversor1.EA_hoy"
    ns6 = "ns=2;s=Inversor1.vs1"
    ns8 = "ns=2;s=Inversor1.vs2"
    ns10 = "ns=2;s=Inversor1.vs3"
    ns12 = "ns=2;s=Inversor1.vs4"
    ns14 = "ns=2;s=Inversor1.vs5"
    ns16 = "ns=2;s=Inversor1.vs6"
    ns18 = "ns=2;s=Inversor1.vs7"
    ns20 = "ns=2;s=Inversor1.vs8"
    ns22 = "ns=2;s=Inversor1.vs9"
    ns24 = "ns=2;s=Inversor1.vs10"
    
    vs_min_val = 500
    vs_max_val = 700

    # populating our address space
    # server.nodes, contains links to very common nodes like objects and root
    myobj = await server.nodes.objects.add_object(idx, "MyObject")
    Inversor1_PA = await myobj.add_variable(ns, "PA", 10.5)
    Inversor1_EA = await myobj.add_variable(ns2, "EA", 26.7)
    Inversor1_EA_hoy = await myobj.add_variable(ns4, "EA_hoy", 0.0)

    Inversor1_vs1 = await myobj.add_variable(ns6, "vs1", 0.0)
    Inversor1_vs2 = await myobj.add_variable(ns8, "vs2", 0.0)
    Inversor1_vs3 = await myobj.add_variable(ns10, "vs3", 0.0)
    Inversor1_vs4 = await myobj.add_variable(ns12, "vs4", 0.0)
    Inversor1_vs5 = await myobj.add_variable(ns14, "vs5", 0.0)
    Inversor1_vs6 = await myobj.add_variable(ns16, "vs6", 0.0)
    Inversor1_vs7 = await myobj.add_variable(ns18, "vs7", 0.0)
    Inversor1_vs8 = await myobj.add_variable(ns20, "vs8", 0.0)
    Inversor1_vs9 = await myobj.add_variable(ns22, "vs9", 0.0)
    Inversor1_vs10 = await myobj.add_variable(ns24, "vs10", 0.0)

    # Set MyVariable to be writable by clients
    await Inversor1_PA.set_writable()
    await Inversor1_EA.set_writable()
    await Inversor1_EA_hoy.set_writable()
    await Inversor1_vs1.set_writable()
    await Inversor1_vs2.set_writable()
    await Inversor1_vs3.set_writable()
    await Inversor1_vs4.set_writable()
    await Inversor1_vs5.set_writable()
    await Inversor1_vs6.set_writable()
    await Inversor1_vs7.set_writable()
    await Inversor1_vs8.set_writable()
    await Inversor1_vs9.set_writable()
    await Inversor1_vs10.set_writable()
    opcs = [ Inversor1_vs1, Inversor1_vs2, Inversor1_vs3, Inversor1_vs4, Inversor1_vs5, Inversor1_vs6, Inversor1_vs7, Inversor1_vs8, Inversor1_vs9, Inversor1_vs10 ]
  
    _logger.info("Starting server!")
    async with server:
        while True:
            await asyncio.sleep(1)
            for opc in opcs:
                random_counter = random.uniform(vs_min_val, vs_max_val)
                new_val = round(random_counter,2)
                #_logger.info("Set value of %s to %.1f", opc, new_val)
                await opc.write_value(new_val)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)