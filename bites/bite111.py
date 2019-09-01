import requests
import json

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    with requests.Session() as s:
        response =  s.get(IPINFO_URL.format(ip=ip_address))
        
        try:
            # data = json.loads(response.text)
            data = response.json()
        except json.JSONDecodeError:
            # recall that json.JSONDecodeError is a subclass of ValueError
            print(f"JSON Decode Error")
        return data["country"]
        
    
if __name__ == "__main__":
    print(get_ip_country("187.190.38.36"))
    print(get_ip_country('185.161.200.10'))


# tests
import json
from unittest.mock import patch, Mock

import requests

from ipinfo import get_ip_country


@patch.object(requests, 'get')
def test_ipinfo_mexican_ip(mockget):
    # hardcoding a requests response
    content = (b'{\n  "ip": "187.190.38.36",\n  "hostname": "domain.net",\n'
               b'  "city": "Mexico City",\n  "region": "Mexico City",\n  '
               b'"country": "MX",\n ' b'"loc": "11.0000,-00.1111",\n  '
               b'"postal": "12345",\n  "org": "some org"\n}')
    mockget.return_value = Mock(content=content,
                                text=content.decode("utf-8"),
                                json=lambda: json.loads(content),
                                status_code=200)
    assert get_ip_country('187.190.38.36') == 'MX'


@patch.object(requests, 'get')
def test_ipinfo_japan_ip(mockget):
    # and another IP in Japan
    content = (b'{\n  "ip": "185.161.200.10",\n  "city": "Tokyo",\n  '
               b'"region": "Tokyo",\n ' b'"country": "JP",\n  "loc": '
               b'"00.1111,11.0000",\n  "postal": "123-4567",\n  '
               b'"org": "some other org"\n}')
    mockget.return_value = Mock(content=content,
                                text=content.decode("utf-8"),
                                json=lambda: json.loads(content),
                                status_code=200)
    assert get_ip_country('185.161.200.10') == 'JP'