# Breaching AD 

these are my notes for the THM Breaching AD room

[https://tryhackme.com/room/breachingad](https://tryhackme.com/room/breachingad)

### Learning Objectives

In this network, we will cover several methods that can be used to breach AD. This is by no means a complete list as new methods and techniques are discovered every day. However, we will  cover the following techniques to recover AD credentials in this network:

- NTLM Authenticated Services
- LDAP Bind Credentials
- Authentication Relays
- Microsoft Deployment Toolkit
- Configuration Files

**don't forget to enable the breaching_ad ovpn file or download if from the networks tab on the access page from tryhackme**

NetNTLM typically uses with Non 3rd party systems like OWA RDP, or even VPN endpoints interagrated with AD and web applications
NTLM passes a challenge-resposne to AD to authenticate the user thus it never has your credentials only the AD controller does
![](screenshots/ntlm_auth.png)

LDAP popular with 3rd party applications that use AD
- Gitlab
- Jenkins
- Custom Web Apps
- printers
- VPNs

LDAP has its own set of AD Credentials it uses to authenticate directly and verify your creds are vaild. this gives you new attack vectors (you could get the applicatons username and password :) )

![](screenshots/ldap_auth.png)

"These credentials are often stored in plain text in configuration files since the security model relies on keeping the location and storage configuration file secure rather than its contents."

you can create your own rouge ldap server using slapd and ldap-utils

*tryhackme attackbox is running - slapd/bionic-updates,bionic-security 2.4.45+dfsg-1ubuntu1.11 amd64 [upgradable from: 2.4.45+dfsg-1ubuntu1.10]
  OpenLDAP server (slapd)*
![](screenshots/attackbox_slapd.png)


ldap passback creds
- za.tryhackme.com\svcLDAP
- tryhackmeldappass1@