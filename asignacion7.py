import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
pprint(payload)
<<<<<<< HEAD
=======

response2 = requests.get(
    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
    headers={'X-Auth-Token':payload['Token']})
payload2 = response2.json()['response']
nameList = []
for i in range(len(payload2)):
    nameList.append([payload2[i]['family'],payload2[i]['hostname'],payload2[i]['managementIpAddress'],payload2[i]['lastUpdated'],payload2[i]['reachabilityStatus']])
pprint(nameList)

>>>>>>> practica
