'''
LNLS 2018 - guilherme.semissatto@lnls.br
'''
import socket
hostCounter = 0
def lookup(addr):
    global hostCounter
    try:
        name, alias, ipaddrlist = socket.gethostbyaddr(addr)
        ipaddrlist = str(ipaddrlist)
        dict_ips[name] = ipaddrlist[2:len(ipaddrlist)-2]
        #print '{0: <60}'.format(name) + "| " + ipaddrlist[2:len(ipaddrlist)-2]
        hostCounter += 1
    except socket.herror:
        return None, None, None

#   Encontra IP e define sub-rede da maquina que executa este codigo, assume-se conexao com Internet
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
machine_ip = s.getsockname()[0]
s.close()
splited_machine_ip = machine_ip.split('.')
subnet = splited_machine_ip[0]+'.'+splited_machine_ip[1]+'.'+splited_machine_ip[2]+'.'

# Cria dicionario de hostname : IP
dict_ips = {}

# Varre todos IPs da sub-rede identificada. Assumindo mascara de sub-rede como 255.255.255.0 (padrao)
for i in range(256):
    addr = subnet + str(i)
    lookup(addr)

# Organiza e imprime dicionario em ordem alfabetica de hostnames
hostnames = dict_ips.keys()
hostnames.sort()

for key in hostnames:
    print '{0: <60}'.format(key) + "| " + dict_ips[key] 
print "Hosts found:", hostCounter
