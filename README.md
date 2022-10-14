# Fintoc
  
Module to connect to Fintoc  

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module

1. You must previously obtain the link_token of the links that have connected to your Fintoc account. Queries on the links that are made from the module will always return the link_token with Null value, so you can not get the link_token of a link that has already been connected. These link_token can only be obtained once, if the link_token is lost, you must reconnect the link with your Fintoc account. 
2. In order to connect, you will need to consult your Secret key from the API Keys section of your Fintoc account.


## Overview


1. Login Fintoc  
Connect with Fintoc using your Secret Key

2. List Links  
Lists all the Links you have created. The listed Links are returned in order, with the last Link created being the first.

3. Retrieve Link  
Get the details of a Link, including associated accounts and their balances.

4. List Invoices  
List all invoices

5. List Accounts  
List all accounts associated to a Link

6. Retrieve Account  
Retrieve an account by its ID.

7. List Movements  
Retrieve a list of movements from a given account.

8. Retrieve Movement  
Retrieve a movement by its ID and the ID of the account it belongs to.  




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