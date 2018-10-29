import socket
socket.settimeout(0.5)
def lookup(addr):
    try:
        name, alias, ipaddrlist = socket.gethostbyaddr(addr)
        ipaddrlist = str(ipaddrlist)
        print ('{0: <60}'.format(name) + "| " + ipaddrlist[2:len(ipaddrlist)-2])

    except socket.herror:
        return None, None, None

#   Encontra IP e define sub-rede da maquina que executa este codigo, assume-se conexao com Internet
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
machine_ip = s.getsockname()[0]
s.close()
splited_machine_ip = machine_ip.split('.')
subnet = splited_machine_ip[0]+'.'+splited_machine_ip[1]+'.'+splited_machine_ip[2]+'.'


#   Varre todos IPs da sub-rede identificada
for i in range(256):
    addr = subnet + str(i)
    lookup(addr)

