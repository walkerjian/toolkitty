
import socket
import requests
import subprocess
import platform
from ipwhois import IPWhois

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def check_https(url):
    try:
        response = requests.get(url)
        return response.url.startswith("https://")
    except requests.exceptions.RequestException:
        return False

def traceroute(host):
    os_name = platform.system()
    if os_name == "Windows":
        command = ['tracert', host]
    else:
        command = ['traceroute', host]
    
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.decode('utf-8').splitlines()
        else:
            return []
    except Exception:
        return []

def geolocate_ip(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        return res['asn_country_code'], res['asn_description']
    except Exception:
        return "Unknown", "Unknown"
