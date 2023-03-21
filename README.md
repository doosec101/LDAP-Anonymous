# LDAP-Anonymous
This script checks for anonymous access login at ldap port 389 only.

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy. This is a legacy configuration, and as of Windows Server 2003, only authenticated users are permitted to initiate LDAP requests.

## Clone & Usage
1. git clone https://github.com/doosec101/LDAP-Anonymous.git
2. cd LDAP-Anonymous/
3. pip3 install requirements.txt
4. python3 LDAP-Anonymous.py -d example.com

## POC:-

![poc](https://user-images.githubusercontent.com/128431701/226491624-bce142d9-17bd-4578-89ad-437f215e83b9.jpg)

## References
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap
- https://sourceforge.net/projects/ldapadmin/
