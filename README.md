# ZCrypt
## Basic decryption tool

### Author's Note
ZCrypt is a basic decryption tool for all CTF enthusiasts especially for Crypto-analysts which covers XOR and RSA techniques. 
### Features
  #### RSA Attacks
  * (c,n,e)
  * (c,p,q,e)
  * (c,n,e,{p or q})
  * (c,n,d)
  * (c1,c2,c3,n1,n2,n3)   [Hasted Broadcast Attack]
  * (c,e)                 [Small Exponent("e") Attack]
  * (c,p,q,dp,dq)         [Chinese Remainder Theorem]
  
  #### XOR
  * Single Byte XOR
  * Repeating Key XOR

Many updates are going to release in future.

### Installation
```
git clone https://github.com/malladisiddu/ZCrypt.git
```
### Requirements
```
cd ZCrypt
apt install libgmp-dev libmpfr-dev libmpc-dev
pip3 install -r requirements.txt 
```
### Usage
```
python3 ZCrypt.py
``` 
