# Fintoc
  
Módulo para conexão com Fintoc  

*Read this in other languages: [English](Manual_Fintoc.md), [Portugues](Manual_Fintoc.pr.md), [Español](Manual_Fintoc.es.md).*
  
![banner](imgs/Banner_Fintoc.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  


## Como usar este módulo

1. Você deve obter previamente o link_token dos Links que tenham conectado com sua conta do Fintoc. As consultas sobre os links que sejam feitas a partir do módulo sempre retornarão o link_token com valor Null, por isso não é possível obter o link_token de um link que já tenha sido conectado. Estes link_token só podem ser obtidos uma vez, se o link_token for perdido, você deve reconectar o link com sua conta do Fintoc.}
2. Para poder se conectar, você deve consultar sua Secret key na seção de API Keys de sua conta do Fintoc.


## Descrição do comando

### Login Fintoc
  
Conecte-se com Fintoc usando sua Secret Key
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Secret Key|Secret Key de Fintoc|sk_test_9c8d8CeyBTx1VcJzuDgpm4H-bywJCeSx|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Listar Links
  
Enumera todos os Links que você criou. Os Links listados são retornados em ordem, sendo o último Link criado o primeiro.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Estado do Link|Uma string que contém o status dos Links que você deseja na resposta.|active|
|Obter apenas o ID|Marque para obter apenas o ID e não toda a informação dos links.|True|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Obter Link
  
Obtenha os detalhes de um Link, incluindo contas associadas e seus saldos.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Link Token|Token do Link a ser obtido.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Listar Faturas
  
Listar todas as faturas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Link Token|Token do Link que contém as Faturas a listar.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Listar Contas
  
Lista todas as contas associadas a um Link
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Link Token|Token do Link que contém as contas a listar.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Obter apenas o ID|Marque para obter apenas o ID e não toda a informação das contas.|True|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Obter Conta
  
Obter uma conta por seu ID.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Conta|ID da conta que deseja obter.|acc_qNDRKQeTpbAKvpnW|
|Link Token|Token do Link que contém as contas a listar.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Listar Movimentos
  
Obtém uma lista de movimentos de uma conta dada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Conta|ID da conta da qual deseja obter os movimentos.|acc_qNDRKQeTpbAKvpnW|
|Link Token|Link Token associado à conta da qual deseja obter os movimentos.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Obter apenas o ID|Marque para obter apenas o ID e não toda a informação das contas.|True|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Obter Movimento
  
Obtenha um movimento por seu ID e o ID da conta a que pertence.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Movement ID|Movement ID|mov_QEaeq4Hyq3PO8mWb|
|ID da Conta|ID da conta que contém o movimento|acc_qNDRKQeTpbAKvpnW|
|Link Token|Link Token associado à conta da qual deseja obter o movimento.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|
