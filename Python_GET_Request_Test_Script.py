# This is a small script for penetration testing
# The script sends a request to a destination IP / Host
# The host header contains a different host
# This being a python script and not a browser, this does not have the SNI extension in the Client Hello

import requests

ip = '93.184.216.34' # This is the actual destination

session = requests.session()

headers = {
'host': 'www.reddit.com' # The host header contains a different destination hostname
}

proxies = { 'http': 'http://127.0.0.1:8888' } # This is required to get the traffic to a proxy such as Fiddler / Charles

request = session.get(f'https://{ip}', verify=True, headers=headers, proxies=proxies) 