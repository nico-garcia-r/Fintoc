# Fintoc
  
Módulo para conectarse a Fintoc  

*Read this in other languages: [English](Manual_Fintoc.md), [Portugues](Manual_Fintoc.pr.md), [Español](Manual_Fintoc.es.md).*
  
![banner](imgs/Banner_Fintoc.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este modulo

1. Se debe obtener previamente el link_token de los Links que hayan conectado con su cuenta de Fintoc. Las consultas sobre los links que se realicen desde el módulo siempre devolverán el link_token con valor Null, por lo que no se puede obtener el link_token de un link que ya se haya conectado. Estos link_token sólamente se pueden obtener una vez, si se pierde el link_token, se debe volver a conectar el link con su cuenta de Fintoc. 
2. Para poder conectarse, deberán consultar su Secret key desde la sección de API Keys de su cuenta de Fintoc.


## Descripción de los comandos

### Login Fintoc
  
Conecta con Fintoc utilizando tu Secret Key
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Secret Key|Secret Key de Fintoc|sk_test_9c8d8CeyBTx1VcJzuDgpm4H-bywJCeSx|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Listar Links
  
Enumera todos los Links que has creado. Los Links listados se devuelven ordenados, siendo el último Link creado el primero.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Estado de Link|Una cadena que contiene el estado de los Links que desea en la respuesta.|active|
|Obtener unicamente el ID|Marca para obtener unicamente el ID y no toda la información de los links.|True|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Obtener Link
  
Obtiene los detalles de un Link, incluyendo las cuentas asociadas y sus saldos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Link Token|Token del Link que se desea obtener.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Listar Facturas
  
Listar todas las facturas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Link Token|Token del Link que contiene las Facturas a listar.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Listar Cuentas
  
Lista todas las cuentas asociadas a un Link
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Link Token|Token del Link que contiene las Cuentas a listar.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Obtener unicamente el ID|Marca para obtener unicamente el ID y no toda la información de las cuentas.|True|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Obtener Cuenta
  
Obtener una cuenta por su ID.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Cuenta|ID de la cuenta que se desea obtener.|acc_qNDRKQeTpbAKvpnW|
|Link Token|Token del Link que contiene las Cuentas a listar.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Listar Movimientos
  
Obtiene una lista de movimientos de una cuenta dada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la Cuenta|ID de la cuenta de la cual se desea obtener los movimientos.|acc_qNDRKQeTpbAKvpnW|
|Link Token|Link Token asociado a la cuenta de la cual se desea obtener los movimientos.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Obtener unicamente el ID|Marca para obtener unicamente el ID y no toda la información de las cuentas.|True|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|

### Obtener Movimiento
  
Obtiene un movimiento por su ID y el ID de la cuenta a la que pertenece.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Movement ID|ID del movimiento|mov_QEaeq4Hyq3PO8mWb|
|ID de la Cuenta|ID de la cuenta la cual contiene el movimiento|acc_qNDRKQeTpbAKvpnW|
|Link Token|Link Token asociado a la cuenta de la cual se desea obtener el movimiento.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Asignar resultado a variable|Asignar resultado de la conexión a variable|result|
