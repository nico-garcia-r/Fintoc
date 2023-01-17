# Fintoc
  
Módulo para conexão com Fintoc  

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  


## Como usar este módulo

1. Você deve obter previamente o link_token dos Links que tenham conectado com sua conta do Fintoc. As consultas sobre os links que sejam feitas a partir do módulo sempre retornarão o link_token com valor Null, por isso não é possível obter o link_token de um link que já tenha sido conectado. Estes link_token só podem ser obtidos uma vez, se o link_token for perdido, você deve reconectar o link com sua conta do Fintoc.}
2. Para poder se conectar, você deve consultar sua Secret key na seção de API Keys de sua conta do Fintoc.

## Overview


1. Login Fintoc  
Conecte-se com Fintoc usando sua Secret Key

2. Listar Links  
Enumera todos os Links que você criou. Os Links listados são retornados em ordem, sendo o último Link criado o primeiro.

3. Obter Link  
Obtenha os detalhes de um Link, incluindo contas associadas e seus saldos.

4. Listar Faturas  
Listar todas as faturas

5. Listar Contas  
Lista todas as contas associadas a um Link

6. Obter Conta  
Obter uma conta por seu ID.

7. Listar Movimentos  
Obtém uma lista de movimentos de uma conta dada.

8. Obter Movimento  
Obtenha um movimento por seu ID e o ID da conta a que pertence.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**python-requests**](https://pypi.org/project/python-requests/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)