from ftplib import FTP
import sqlite3

conn = sqlite3.connect('MiCLoudPrivada')
c = conn.cursor()


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

cont1 = 0
host = '192.168.0.101'
port = 5000
user = 'admin1'
password = 'admin1'
ftp = FTP()
ftp.connect(host, port)
ftp.login(user, password)
print(ftp.getwelcome())
c.execute("SELECT id FROM usuariosFTP")
i = c.fetchall()
for n in i:
    c.execute("SELECT usuario FROM usuariosFTP")
    usuarioAUX = c.fetchall()
    usuario = listToString(usuarioAUX[cont1])
    print(usuario)
    if usuario in ftp.nlst():
        print("ya existe")
    else:
        ftp.mkd(usuario)
    cont1 = cont1+1
    print(n)

print(ftp.pwd())




