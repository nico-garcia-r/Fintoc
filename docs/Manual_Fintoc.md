# Fintoc
  
Module to connect to Fintoc 

*Read this in other languages: [English](Manual_Fintoc.md), [Portugues](Manual_Fintoc.pr.md), [Español](Manual_Fintoc.es.md).*
  
![banner](imgs/Banner_Fintoc.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module

1. You must previously obtain the link_token of the links that have connected to your Fintoc account. Queries on the links that are made from the module will always return the link_token with Null value, so you can not get the link_token of a link that has already been connected. These link_token can only be obtained once, if the link_token is lost, you must reconnect the link with your Fintoc account. 
2. In order to connect, you will need to consult your Secret key from the API Keys section of your Fintoc account.


## Description of the commands

### Login Fintoc
  
Connect with Fintoc using your Secret Key
|Parameters|Description|example|
| --- | --- | --- |
|Secret Key|Fintoc Secret Key|sk_test_9c8d8CeyBTx1VcJzuDgpm4H-bywJCeSx|
|Assign result to variable|Assign connection result to variable|result|

### List Links
  
Lists all the Links you have created. The listed Links are returned in order, with the last Link created being the first.
|Parameters|Description|example|
| --- | --- | --- |
|Link Status|A string that contains the status of the Links you want in the response.|active|
|Get only the ID|Check to get only the ID and not all the information of the links.|True|
|Assign result to variable|Assign connection result to variable|result|

### Retrieve Link
  
Get the details of a Link, including associated accounts and their balances.
|Parameters|Description|example|
| --- | --- | --- |
|Link Token|Token of the Link to be obtained.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Assign result to variable|Assign connection result to variable|result|

### List Invoices
  
List all invoices
|Parameters|Description|example|
| --- | --- | --- |
|Link Token|Token of the Link that contains the Invoices to list.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Assign result to variable|Assign connection result to variable|result|

### List Accounts
  
List all accounts associated to a Link
|Parameters|Description|example|
| --- | --- | --- |
|Link Token|Token of the Link that contains the Accounts to list.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Get only the ID|Check to get only the ID and not all the information of the accounts.|True|
|Assign result to variable|Assign connection result to variable|result|

### Retrieve Account
  
Retrieve an account by its ID.
|Parameters|Description|example|
| --- | --- | --- |
|Account ID|ID of the account to be retrieved.|acc_qNDRKQeTpbAKvpnW|
|Link Token|Token of the Link that contains the Accounts to list.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Assign result to variable|Assign connection result to variable|result|

### List Movements
  
Retrieve a list of movements from a given account.
|Parameters|Description|example|
| --- | --- | --- |
|Account ID|ID of the account from which you want to get the movements.|acc_qNDRKQeTpbAKvpnW|
|Link Token|Link Token associated with the account from which you want to get the movements.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Get only the ID|Check to get only the ID and not all the information of the accounts.|True|
|Assign result to variable|Assign connection result to variable|result|

### Retrieve Movement
  
Retrieve a movement by its ID and the ID of the account it belongs to.
|Parameters|Description|example|
| --- | --- | --- |
|Movement ID|Movement ID|mov_QEaeq4Hyq3PO8mWb|
|Account ID|Account ID which contains the movement|acc_qNDRKQeTpbAKvpnW|
|Link Token|Link Token associated with the account from which you want to get the movement.|link_Q0xVGPvijElLRMwE_token_FhsFVurz5q5FycHA5xxhTpzX|
|Assign result to variable|Assign connection result to variable|result|
