# New IP TOR
[![Python 3.7](https://img.shields.io/badge/Python-3.7-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Mac-orange.svg)]()
![GitHub](https://img.shields.io/github/license/MrCl0wnLab/new-ip-tor?color=blue)

```
 + Autor: MrCl0wn
 + Blog: http://blog.mrcl0wn.com
 + GitHub: https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email: mrcl0wnlab\@\gmail.com
```
## WARNING
```
+------------------------------------------------------------------------------+
|  [!] Legal disclaimer: Usage of afdWordpress for attacking                   |
|  targets without prior mutual consent is illegal.                            |
|  It is the end user's responsibility to obey all applicable                  | 
|  local, state and federal laws.                                              |
|  Developers assume no liability and are not responsible for any misuse or    |
|  damage caused by this program                                               |
+------------------------------------------------------------------------------+
```
### DESCRIPTION
```
This module makes it easy to reboot IP Tor network
```
### REQUIREMENTS
```
os
datetime
requests
threading
time
```
### Implementation
```python
import tor
import requests

url_list = [
    'https://www.fbi.gov',
    'http://www.abin.gov.br',
    'https://www.mossad.gov.il',
    'https://www.cia.gov',
    'https://www.nsa.gov',
]

for url in url_list:
    tor.new_ip_tor()
    # tor.DEBUG = True
    result = requests.get(url)
    print('[+]', url, result.status_code)
```
