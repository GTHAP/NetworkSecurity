# This is a small script for penetration testing
# The script sends a request to a destination IP / Host
# The host header contains a different host
# This being a Python script and not a browser, this does not have the SNI extension in the Client Hello
# FYI, this only works when there is a proxy in the picture and a CONNECT request is sent to connect to the proxy

import requests
ip = '20.207.73.82' # Github IP address
s = requests.session()
headers = {'host': 'www.example.com'}
# When using Fiddler Proxy (to catch HTTP requests) us the three lines below and comment out lines 9 and 10
# proxies = { 'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888' }
# r = s.get(f'https://{ip}', proxies=proxies, verify=False, headers=headers)
# r1 = s.get(f'https://{ip}/explore', proxies=proxies, verify=False, headers=headers)
r = s.get(f'https://{ip}', verify=False, headers=headers) # The URL has the Github IP and the Host header has www.example.com
r1 = s.get(f'https://{ip}/explore', verify=False, headers=headers)
print(r, r1)
