# Servidor OPC-UA

### 0. Introducción

En este docker se creará un servidor OPC-UA sin encriptación y anónimo en Python3 con la librería "asyncua". En el servidor se han creado tres objetos:

| Objeto | Id | TipoDato | Descripción | 
| :----: | :----: | :----: | :----: |  
| PA | ns=2;s=Inversor1.PA | Doble | No se actualiza automáticamente |
| EA | ns=2;s=Inversor1.EA | Doble | No se actualiza automáticamente |
| EA_hoy | ns=2;s=Inversor1.EA_hoy | Doble | No se actualiza automáticamente |
| Vs1 | ns=2;s=Inversor1.vs1 | Doble | Se trata de una variable que se actualiza cada segundo |

Mediante el docker de Jupyter-Notebook se pueden consultar estos valores y escribirlos

### 1. Microservicios empleados

| Microservicio      | Descripción | Puerto | GUI |
| :----:             |    :----:   |    :----:   |   :----:   |
| Server    | Servidor OPC-UA        | 4840 | - |
| BBDD    | Postgres        | 5432 | - |
| API   | API  | 8888 | http://localhost/docs |
| Jupyter Notebook   | Plataforma web para realizar operar OPC-UA como cliente  | 8888 | http://localhost:8888 |

### 2. Levantar los contenedores
```docker compose up -d```

### 3. Comprobamos que se ha montado correctamente el servidor OPC-UA

Cuando se accede al servidor se pueden ver los tres objetos creados y leer el valor actual y escribirlos. Recordar que como la tensión y la presión se actualiza automáticamente no se puede quedará el valor escrito.

![Architecture](pantallazo.png)

### 4. Accedemos a jupyter notebook

```http://localhost:8888```

### 5. Ejecutamos los siguientes Scripts

| Script      | Descripcion | 
| :----:             |    :----:   |
| Client_Read    | El Script lee varias varibles del server OPC-UA       | 
| Client_Write   | El scropt escribe varias variables del server OPC-UA       |


https://github.com/FreeOpcUa/python-opcua/tree/master