"""R11-05 requests verify=False, urllib3 warning disabled, ssl unverified context, paramiko AutoAddPolicy."""
import ssl

import paramiko
import requests
import urllib3

urllib3.disable_warnings()
requests.get("https://partner.qx.example.com", verify=False)       # TLS verification OFF
ctx = ssl._create_unverified_context()                             # unverified SSL context

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())       # accepts any SSH host key
