# Servidor OPC-UA

En este docker se crear un servidor OPC-UA sin encriptación y anonimo en Python3 con la libreria "asyncua". En el servidor se han creado tres objetos:

| Objeto | Id | Descripcion | 
| :----: | :----: | :----: |  
| Presion | ns=2;s=freeopcua.Tags.pressure | Se trata de una variable int64 que se actualiza cada segundo |
| Temperatura | ns=2;s=freeopcua.Tags.pressure | Se trata de una variable int64 que se actualiza cada segundo |
| Tension | ns=2;s=freeopcua.Tags.voltage | No se actualiza autoamticamente |

Mediante el docker de Jupyter-Notebook se pueden consultar estos valores y escribirlos

### 0. Microservicios empleados

| Microservicio      | Descripcion |  GUI |
| :----:             |    :----:   |    :----:   |
| Python3    | Servidor OPC-UA        | - |
| Jupyter Notebook   | Plataforma web para realizar operar OPC-UA como cliente  | http://localhost:8888 |


### 1. Levantar los contenedores
```docker compose up -d```

### 2. Accedemos a jupyter notebook

```http://localhost:8888```

### 3. Ejecutamos los siguientes Scripts

| Script      | Descripcion | 
| :----:             |    :----:   |
| Client_Read    | El Script lee varias varibles del server OPC-UA       | 
| Client_Write   | El scropt escribe varias variables del server OPC-UA       |