import socket

def get_ips_for_host(host):
        try:
            ips = socket.gethostbyname_ex(host)
        except socket.gaierror:
            ips=[]
        return ips

host = input ("Enter the URL for a host: ")
ips = get_ips_for_host(host)
print(ips[2])