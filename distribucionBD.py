import socket, os

print os.popen("mysqldump --user=root --password=anamartinez45 empresa > /home/anna/Documentos/Respaldo/respaldo5.sql")
