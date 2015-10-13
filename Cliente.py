import socket, os

os.popen("mysqldump --user=root --password=diana empresa > /home/diana/Documentos/Sombra.sql")

ruta = "/home/diana/Documentos/"
filename = "Diana.sql"
HOST = "192.168.50.2"

CPORT = 9090
FPORT = 9091

control = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
control.connect((HOST,CPORT))
control.send("SEND" + filename)
control.close()
archivo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
archivo.connect((HOST,FPORT))

f = open (ruta+filename,"rb")
datos = f.read()
f.close()


archivo.send(datos)
archivo.close()
